# QMT 本机 HTTP 桥

miniQMT 不可用时，外面的 Python 进程仍要查行情、对持仓。本仓库是一份最小工程示例：在 **大 QMT** 里用自带的 tornado 起本机 HTTP，外部用 token 调函数。

只监听 `127.0.0.1:18765`。不要改成 `0.0.0.0`，也不要映射到公网。

不构成投资建议。不代操盘。`passorder` 返回不等于成交。

## 文件

| 文件 | 放哪 |
| --- | --- |
| `qmt_bridge.py` | QMT 策略编辑器，用「运行」启动 |
| `client_example.py` | 本机另一份 Python 3 |

首次启动会在同目录生成 `qmt_bridge.token`。外部请求头带 `X-Bridge-Token`。

## 接口

- `GET /health` 不校验 token，只看进程在不在
- `POST /v1/quote/tick`  body `{"codes":["600000.SH"]}`
- `POST /v1/account/book`  打印可用资金和持仓，用于对账
- `POST /v1/order/pass`  薄封装 `passorder`，必须 `confirm=yes`；自行对文档填参数

手册：https://www.kimiquant.cn/qmt/

## 注意

1. `IOLoop` 放后台线程，避免 `init` 里 `start()` 卡住 `handlebar`。
2. QMT 内置 Python 约 3.6，不要写 3.10 语法。
3. 上交所代码用 `.SH`。
4. 令牌文件不要提交 git。

## 许可

MIT
