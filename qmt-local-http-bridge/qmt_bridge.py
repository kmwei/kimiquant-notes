#coding:gbk
"""QMT 本机 HTTP 桥（放进策略编辑器，在「运行」里启动）。

只监听 127.0.0.1。令牌写在同目录 qmt_bridge.token。
IOLoop 放后台线程，避免 init 里 start() 把 handlebar 卡死。
不构成投资建议，不代操盘。
"""
from __future__ import print_function

import json
import os
import threading
import traceback

from tornado.ioloop import IOLoop
from tornado.web import Application, HTTPError, RequestHandler

LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = 18765
ACCOUNT_TYPE = "STOCK"
STRATEGY_NAME = "local_http_bridge"


def token_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "qmt_bridge.token")


def load_or_make_token():
    path = token_path()
    if os.path.exists(path):
        with open(path, "r") as f:
            text = f.read().strip()
        if text:
            return text
    raw = os.urandom(16)
    text = "".join("%02x" % (b if isinstance(b, int) else ord(b)) for b in raw)
    with open(path, "w") as f:
        f.write(text)
    print("[bridge] token written:", path)
    return text


def safe_call(fn, *args, **kwargs):
    try:
        return True, fn(*args, **kwargs), ""
    except Exception:
        return False, None, traceback.format_exc()


class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=utf-8")

    def prepare(self):
        expect = self.application.bridge_token
        got = self.request.headers.get("X-Bridge-Token", "")
        if not expect or got != expect:
            raise HTTPError(401, "token mismatch")

    def ctx(self):
        return self.application.qmt_ctx

    def acc(self):
        return self.application.account_id

    def read_json(self):
        body = self.request.body or b"{}"
        if not body:
            return {}
        return json.loads(body.decode("utf-8"))

    def dump(self, payload, status=200):
        self.set_status(status)
        self.write(json.dumps(payload, ensure_ascii=False, default=str))


class HealthHandler(BaseHandler):
    def prepare(self):
        return

    def get(self):
        self.dump({"ok": True, "host": LISTEN_HOST, "port": LISTEN_PORT})


class TickHandler(BaseHandler):
    def post(self):
        data = self.read_json()
        codes = data.get("codes") or []
        if isinstance(codes, str):
            codes = [x.strip() for x in codes.split(",") if x.strip()]
        if not codes:
            raise HTTPError(400, "codes required")
        ok, ret, err = safe_call(self.ctx().get_full_tick, codes)
        if not ok:
            self.dump({"ok": False, "error": err}, 500)
            return
        self.dump({"ok": True, "data": ret or {}})


class BookHandler(BaseHandler):
    def post(self):
        acc_type = self.read_json().get("account_type") or ACCOUNT_TYPE
        acc_ok, accts, acc_err = safe_call(
            get_trade_detail_data, self.acc(), acc_type, "ACCOUNT"
        )
        pos_ok, poss, pos_err = safe_call(
            get_trade_detail_data, self.acc(), acc_type, "POSITION"
        )
        book = {"account": [], "positions": []}
        if acc_ok:
            for a in accts or []:
                book["account"].append(
                    {
                        "available": getattr(a, "m_dAvailable", None),
                        "balance": getattr(a, "m_dBalance", None),
                    }
                )
        if pos_ok:
            for p in poss or []:
                book["positions"].append(
                    {
                        "code": getattr(p, "m_strInstrumentID", ""),
                        "volume": getattr(p, "m_nVolume", None),
                        "can_use": getattr(p, "m_nCanUseVolume", None),
                    }
                )
        self.dump(
            {
                "ok": acc_ok and pos_ok,
                "data": book,
                "error": (acc_err or "") + (pos_err or ""),
            }
        )


class PassorderHandler(BaseHandler):
    """薄封装：原样把参数交给 passorder。返回不等于成交。"""

    def post(self):
        data = self.read_json()
        if data.get("confirm") != "yes":
            raise HTTPError(400, "confirm must be yes")
        stock = data.get("stock")
        if not stock:
            raise HTTPError(400, "stock required")
        op_type = int(data.get("op_type", 23))
        order_type = int(data.get("order_type", 1101))
        pr_type = int(data.get("pr_type", 5))
        price = float(data.get("price", -1))
        volume = int(data.get("volume", 0))
        ok, ret, err = safe_call(
            passorder,
            op_type,
            order_type,
            self.acc(),
            stock,
            pr_type,
            price,
            volume,
            STRATEGY_NAME,
            2,
            "",
            self.ctx(),
        )
        if not ok:
            self.dump({"ok": False, "error": err}, 500)
            return
        self.dump({"ok": True, "passorder_ret": ret, "note": "not a fill"})


def make_app(ctx, account_id, token):
    app = Application(
        [
            (r"/health", HealthHandler),
            (r"/v1/quote/tick", TickHandler),
            (r"/v1/account/book", BookHandler),
            (r"/v1/order/pass", PassorderHandler),
        ]
    )
    app.qmt_ctx = ctx
    app.account_id = account_id
    app.bridge_token = token
    return app


def start_bridge(ctx):
    token = load_or_make_token()
    try:
        account_id = account
    except NameError:
        account_id = ""
    if not account_id:
        print("[bridge] account empty: set it in strategy trade panel")
    app = make_app(ctx, account_id, token)
    app.listen(LISTEN_PORT, address=LISTEN_HOST)
    print("[bridge] http://%s:%s token file %s" % (LISTEN_HOST, LISTEN_PORT, token_path()))
    IOLoop.current().start()


def init(C):
    try:
        C.set_account(account)
    except Exception:
        pass
    t = threading.Thread(target=start_bridge, args=(C,), name="qmt-http-bridge")
    t.daemon = True
    t.start()
    print("[bridge] background thread started")


def handlebar(C):
    if not C.is_last_bar():
        return
    print("[bridge] handlebar still alive")
