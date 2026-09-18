# QMT 报错怎么排：先对现象，再对函数

QMT 的报错原文因券商客户端版本差别很大，**搜报错原文往往搜不到东西**。按现象对页更有效。

| 你看到的情况 | 先看 |
| --- | --- |
| `get_full_tick` / 盘口为空 | [拿不到实时行情](https://www.kimiquant.cn/problems/qmt-no-realtime-tick) |
| 下单返回了但没成交 / 废单 | [passorder 未成交](https://www.kimiquant.cn/problems/qmt-passorder-not-filled) |
| 不知道委托有没有成 | [委托回调怎么写](https://www.kimiquant.cn/problems/qmt-order-callback) |
| 持仓 / 资金查不到 | [怎么获取持仓](https://www.kimiquant.cn/problems/qmt-how-to-get-position) |
| 回测能跑、实盘歪，或反过来 | [回测和实盘不一样](https://www.kimiquant.cn/problems/qmt-backtest-vs-live) |
| `run_time` 回测没日志 | [run_time 回测不跑](https://www.kimiquant.cn/problems/qmt-runtime-backtest) |
| 通用 AI 贴进来就炸 | [AI 写的 QMT 跑不了](https://www.kimiquant.cn/problems/ai-qmt-code) |
| 编码 / `SyntaxError` | 源码第一行加 `#coding:gbk` |
| `not in whitelist` | 自装库不在券商白名单，找营业部 |
| 后缀乱 | [`.SS` 和 `.SH`](https://www.kimiquant.cn/problems/ss-vs-sh) |

## 通用排查顺序

1. 是不是在**策略交易界面**跑，账号绑上了没有
2. 代码后缀、账号类型（`STOCK` / `CREDIT`）对不对
3. 用到的函数在当前模式（回测 / 实盘）支不支持
4. 对手册枚举填 `passorder`，不要凭记忆
5. 还卡住：贴日志给 [AI 修报错](https://www.kimiquant.cn/tools/ai?mode=fix)

完整索引：https://www.kimiquant.cn/problems/
