# QMT 和 PTrade 有什么区别

不是「哪个更好」，是**运行位置、字段、权限**三件事都不一样。选错会在迁移时集中还债。

| 维度 | QMT | PTrade |
| --- | --- | --- |
| 运行位置 | 本机客户端 | 券商服务器托管 |
| 上交所后缀 | `.SH` | `.SS`（或 `.XSHG`） |
| 持仓字段 | `m_nVolume` / `m_nCanUseVolume` | `amount` / `enable_amount` |
| 持仓查询 | `get_trade_detail_data(..., 'POSITION')` | 无 `get_trade_detail_data`，走另一套 |
| 环境 | 内置 Python ≈ 3.6.8，有包白名单 | 托管环境，依赖受限 |
| 关机影响 | 本机不关就一直在跑 | 托管，但受券商策略限制 |

## 常见误解

**「字段名差不多，直接改后缀就行」** —— 不行。字段命名毫无关联，迁移时必须逐个对照。

**「PTrade 托管就不用管机器了」** —— 但托管环境的依赖和 API 受券商限制，能做的事比本机少。

**「两边取行情的方式一样」** —— PTrade 的 `get_snapshot` 大约 3 秒一帧，拿它做日内高频会吃亏。

完整对照：https://www.kimiquant.cn/problems/qmt-vs-ptrade

字段对照表：https://www.kimiquant.cn/notes/position-cash
