# QMT 怎么获取持仓（可用 ≠ 总量）

主动查询用 `get_trade_detail_data`，别去翻有没有「持仓接口」——它就在这个函数里，靠 `strDatatype` 区分。

| `strDatatype` | 拿到什么 |
| --- | --- |
| `POSITION` | 持仓明细 |
| `ACCOUNT` | 资金（可用、余额） |
| `ORDER` / `DEAL` | 当日委托 / 成交 |

账号类型：普通 `STOCK`、两融 `CREDIT`、期货 `FUTURE`。

## 三个最容易踩的点

**1. `m_nCanUseVolume` ≠ `m_nVolume`。** T+1、新买入、挂单冻结都会让可用小于总量。下单前读**可用**，不是总量。

**2. `strategyName` 不过滤持仓。** 它只作用于 `ORDER` / `DEAL`；`POSITION` 和 `ACCOUNT` 返回的**永远是账户级**数据。同一账号挂多个策略时，各自都看到全量持仓——不自己记账就会重复下单。

**3. 回测 / 编辑器里列表为空是正常的。** 没绑真实账号就没有持仓数据。要确认是在**策略交易界面**跑、账号绑上了、类型传对了。

字段名是 `m_` 前缀那一套，版本之间略有差异，拿不准先 `dir(obj)` 打一遍。

完整字段和示例：https://www.kimiquant.cn/problems/qmt-how-to-get-position

QMT / PTrade 字段对照：https://www.kimiquant.cn/notes/position-cash
