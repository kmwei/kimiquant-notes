# -*- coding: utf-8 -*-
"""QMT 本机桥的外部调用示例。在本机 Python 3 跑，不要暴露到公网。"""
from __future__ import print_function

import json
import os

try:
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import HTTPError, Request, URLError, urlopen


class BridgeClient(object):
    def __init__(self, base="http://127.0.0.1:18765", token=""):
        self.base = base.rstrip("/")
        if not token:
            here = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(here, "qmt_bridge.token")
            if os.path.isfile(path):
                with open(path, "r") as f:
                    token = f.read().strip()
        self.token = token

    def _call(self, method, path, payload=None):
        data = None
        headers = {"X-Bridge-Token": self.token}
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json; charset=utf-8"
        req = Request(self.base + path, data=data, headers=headers)
        req.get_method = lambda: method
        try:
            resp = urlopen(req, timeout=10)
            body = resp.read().decode("utf-8")
            return json.loads(body)
        except HTTPError as e:
            return {"ok": False, "http": e.code, "error": e.read().decode("utf-8", "ignore")}
        except URLError as e:
            return {"ok": False, "error": str(e.reason)}

    def health(self):
        return self._call("GET", "/health")

    def tick(self, codes):
        return self._call("POST", "/v1/quote/tick", {"codes": codes})

    def book(self, account_type="STOCK"):
        return self._call("POST", "/v1/account/book", {"account_type": account_type})


if __name__ == "__main__":
    c = BridgeClient()
    print("health", c.health())
    print("tick", c.tick(["600000.SH"]))
    print("book", c.book())
