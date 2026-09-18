# KimiQuant 开发笔记

面向 QMT / PTrade 量化开发的踩坑笔记与选型索引。仓库只放原创短文和可跑示例，**不镜像官方手册**。

完整手册、API 查询和问题页在主站：**https://www.kimiquant.cn**

> 查函数签名请用 [API 快速查询](https://www.kimiquant.cn/tools/api)；本仓库负责「按现象找答案」，主站负责「按函数查用法」。

---

## 先看这几篇

最常被问到、也最容易踩的六个点：

| 主题 | 笔记 | 主站页 |
| --- | --- | --- |
| QMT 拿不到实时行情 | [notes/qmt-no-realtime-tick.md](notes/qmt-no-realtime-tick.md) | [问题页](https://www.kimiquant.cn/problems/qmt-no-realtime-tick) |
| QMT 如何取盘口 | [notes/qmt-how-to-get-quote.md](notes/qmt-how-to-get-quote.md) | [问题页](https://www.kimiquant.cn/problems/qmt-how-to-get-quote) |
| `run_time` 回测不跑 | [notes/qmt-runtime-backtest.md](notes/qmt-runtime-backtest.md) | [问题页](https://www.kimiquant.cn/problems/qmt-runtime-backtest) |
| QMT 委托回调怎么写 | [notes/qmt-order-callback.md](notes/qmt-order-callback.md) | [问题页](https://www.kimiquant.cn/problems/qmt-order-callback) |
| 后缀 `.SS` / `.SH` 搞混 | [notes/ss-vs-sh.md](notes/ss-vs-sh.md) | [问题页](https://www.kimiquant.cn/problems/ss-vs-sh) |
| PTrade 9:30 下单失败 | [notes/ptrade-930-order-fail.md](notes/ptrade-930-order-fail.md) | [问题页](https://www.kimiquant.cn/problems/ptrade-930-order-fail) |

---

## 按现象查问题

### 行情与数据

| 现象 | 主站页 |
| --- | --- |
| 拿不到实时行情 / `get_full_tick` 返回空 | [qmt-no-realtime-tick](https://www.kimiquant.cn/problems/qmt-no-realtime-tick) |
| 不知道怎么取盘口 | [qmt-how-to-get-quote](https://www.kimiquant.cn/problems/qmt-how-to-get-quote) |
| `get_market_data_ex` 和 `get_market_data` 差在哪 | [qmt-get-market-data-ex](https://www.kimiquant.cn/problems/qmt-get-market-data-ex) |
| `get_full_tick` 在回测里不能用 | [qmt-full-tick-backtest](https://www.kimiquant.cn/problems/qmt-full-tick-backtest) |
| 后缀 `.SS` / `.SH` 用错 | [ss-vs-sh](https://www.kimiquant.cn/problems/ss-vs-sh) |

### 下单与委托

| 现象 | 主站页 |
| --- | --- |
| `passorder` 参数不知道填什么 | [qmt-passorder-params](https://www.kimiquant.cn/problems/qmt-passorder-params) |
| 下单函数返回了但没成交 / 废单 | [qmt-passorder-not-filled](https://www.kimiquant.cn/problems/qmt-passorder-not-filled) |
| 不知道委托成没成、回调怎么写 | [qmt-order-callback](https://www.kimiquant.cn/problems/qmt-order-callback) |
| PTrade 9:30 下单失败 | [ptrade-930-order-fail](https://www.kimiquant.cn/problems/ptrade-930-order-fail) |
| 撤单函数怎么用 | [ptrade-cancel-order](https://www.kimiquant.cn/problems/ptrade-cancel-order) |
| 手续费 / 滑点设置不生效 | [ptrade-set-commission-trade](https://www.kimiquant.cn/problems/ptrade-set-commission-trade) |

### 持仓与资金

| 现象 | 主站页 |
| --- | --- |
| 查不到持仓 / 数量和券商对不上 | [notes/qmt-how-to-get-position.md](notes/qmt-how-to-get-position.md) · [主站](https://www.kimiquant.cn/problems/qmt-how-to-get-position) |
| 取可用资金 | [ptrade-get-cash](https://www.kimiquant.cn/problems/ptrade-get-cash) |
| PTrade 没有 `get_trade_detail_data` | [ptrade-no-get-trade-detail-data](https://www.kimiquant.cn/problems/ptrade-no-get-trade-detail-data) |
| `get_snapshot` 大约 3 秒一帧 | [ptrade-snapshot-3s](https://www.kimiquant.cn/problems/ptrade-snapshot-3s) |
| 两套字段对不上（`m_` vs `amount`） | [position-cash](https://www.kimiquant.cn/notes/position-cash) |

### 回测与实盘

| 现象 | 主站页 |
| --- | --- |
| 回测能跑、实盘结果不一样 | [qmt-backtest-vs-live](https://www.kimiquant.cn/problems/qmt-backtest-vs-live) |
| `run_time` 回测里没有日志 | [qmt-runtime-backtest](https://www.kimiquant.cn/problems/qmt-runtime-backtest) |
| `handlebar` 和 `run_time` 该选哪个 | [qmt-handlebar-vs-runtime](https://www.kimiquant.cn/problems/qmt-handlebar-vs-runtime) |

### 排错

| 现象 | 主站页 |
| --- | --- |
| 各类报错，按现象对页 | [notes/qmt-common-errors.md](notes/qmt-common-errors.md) · [主站](https://www.kimiquant.cn/problems/qmt-common-errors) |
| 通用 AI 写出来的 QMT 代码跑不了 | [ai-qmt-code](https://www.kimiquant.cn/problems/ai-qmt-code) |

### 从聚宽 / 通达信迁移

| 现象 | 主站页 |
| --- | --- |
| 策略想继续在聚宽跑，只把单子接到本机 | [jq-follow-qmt](https://www.kimiquant.cn/problems/jq-follow-qmt) |
| 聚宽转 QMT：生命周期、后缀、定时对不上 | [jq-to-qmt](https://www.kimiquant.cn/problems/jq-to-qmt) |
| 聚宽转 PTrade：后缀、持仓、财务对不上 | [jq-to-ptrade](https://www.kimiquant.cn/problems/jq-to-ptrade) |
| 通达信选股公式放到 QMT 里自动跑 | [tdx-to-qmt](https://www.kimiquant.cn/notes/tdx-to-qmt) |

### 选型与权限

| 问题 | 主站页 |
| --- | --- |
| QMT 和 PTrade 有什么区别 | [notes/qmt-vs-ptrade.md](notes/qmt-vs-ptrade.md) · [主站](https://www.kimiquant.cn/problems/qmt-vs-ptrade) |
| PTrade 在不同券商有什么差异 | [ptrade-broker-diff](https://www.kimiquant.cn/problems/ptrade-broker-diff) |
| 只有大 QMT，外部 Python 怎么调函数 | [qmt-local-http-bridge](https://www.kimiquant.cn/problems/qmt-local-http-bridge) |
| 大 QMT 怎么用成 miniQMT（开源 cfquant） | [cfquant-miniqmt-bridge](https://www.kimiquant.cn/notes/cfquant-miniqmt-bridge) |

---

## 接口对照速查

| 主题 | 主站页 |
| --- | --- |
| 历史 K 线：`get_market_data_ex` vs `get_history` | [history-bars](https://www.kimiquant.cn/notes/history-bars) |
| 定时任务对照：`run_time` / `schedule_run` / `run_daily` | [timers](https://www.kimiquant.cn/notes/timers) |
| 日志和「只跑一次」：日期戳 / `C.done` | [run-once](https://www.kimiquant.cn/notes/run-once) |
| 撤单：先查单号再撤 | [cancel](https://www.kimiquant.cn/notes/cancel) |
| 逆回购下单接口 | [reverse-repo](https://www.kimiquant.cn/notes/reverse-repo) |
| 可转债基础信息怎么取 | [convertible-bond](https://www.kimiquant.cn/notes/convertible-bond) |
| 新股申购：两套接口怎么接 | [ipo](https://www.kimiquant.cn/notes/ipo) |

---

## 自动化与盯盘

| 主题 | 主站页 |
| --- | --- |
| 让 QMT 每天自动选股买入 | [qmt-daily-select-buy](https://www.kimiquant.cn/notes/qmt-daily-select-buy) |
| 持仓和异常怎么盯（微信提醒） | [qmt-monitor-wechat](https://www.kimiquant.cn/notes/qmt-monitor-wechat) |
| 聚宽模拟盘信号接到本机 QMT | [jq-signal-qmt](https://www.kimiquant.cn/notes/jq-signal-qmt) |
| 信号同步的延迟优化与实测 | [jq-signal-latency](https://www.kimiquant.cn/notes/jq-signal-latency) |

---

## 策略笔记

同一策略通常有 QMT / PTrade 两版，字段和生命周期不一样，对照着看。

| 策略 | 主站页 |
| --- | --- |
| 小市值（市值排序与空仓月） | [smallcap](https://www.kimiquant.cn/notes/smallcap) · [QMT](https://www.kimiquant.cn/notes/qmt-smallcap) · [PTrade](https://www.kimiquant.cn/notes/ptrade-smallcap) |
| ETF 轮动 | [QMT](https://www.kimiquant.cn/notes/qmt-etf-rotate) · [PTrade](https://www.kimiquant.cn/notes/ptrade-etf-rotate) |
| 七星 ETF 动量轮动 | [qixing-etf](https://www.kimiquant.cn/notes/qixing-etf) |
| 五福 ETF 轮动（动态池与防御） | [wufu-etf](https://www.kimiquant.cn/notes/wufu-etf) |
| 准点对时高频申赎 ETF（毫秒窗口） | [etf-timed-creation](https://www.kimiquant.cn/notes/etf-timed-creation) |
| 涨停基因小市值（涨停密度与周调仓） | [limit-gene](https://www.kimiquant.cn/notes/limit-gene) |
| 低位 3 连阳 · 首板高开 | [low3-sbgk](https://www.kimiquant.cn/notes/low3-sbgk) |
| 固定价差回转（成交后反向挂一档） | [spread-reversal](https://www.kimiquant.cn/notes/spread-reversal) |

---

## 本机 HTTP 桥

券商只给大 QMT、没有 miniQMT / XtQuantServer 时，可以在大 QMT 里起一个**只听 `127.0.0.1`** 的本机 HTTP，让外部 Python 查行情、对持仓。

完整可跑示例见 [qmt-local-http-bridge/](qmt-local-http-bridge/)；说明与踩坑（`init` 里直接启动事件循环会卡住 `handlebar`）见[问题页](https://www.kimiquant.cn/problems/qmt-local-http-bridge)。

---

## 知乎 / 掘金改写稿

`zhihu/` 目录放可直接改写的稿子，文末保留主站链接。以主站页面为准。

---

## 关于

- 本仓库内容以主站页面为准，笔记是精简版。
- 委托「提交成功」不等于成交；示例代码只用于本机研究与对账，不构成投资建议，也不代操盘。
- 账号、密码、令牌请留在本机，不要提交到仓库。
- 策略代写 / 开通咨询走公众号「Kimi量化」：https://www.kimiquant.cn/follow

主站：**https://www.kimiquant.cn** · 问题索引：https://www.kimiquant.cn/problems/ · API 查询：https://www.kimiquant.cn/tools/api
