# QMT 查持仓查不到、数量对不上，先看这三条

`get_trade_detail_data` 是能用的，多数时候是**口径没分清**。

1. **可用 ≠ 总量。** `m_nCanUseVolume` 小于 `m_nVolume` 是正常的：T+1、当天新买入、挂单冻结都会造成差额。下单前读**可用**，不是总量，否则盘中会被「超过可用」拒单。

2. **`strategyName` 不过滤持仓。** 它只作用于 `ORDER` / `DEAL`。`POSITION` 和 `ACCOUNT` 返回的**永远是账户级**数据 —— 同一账号挂多个策略时，各自都看到全量持仓，不自己记账就会重复下单。

3. **回测 / 编辑器里列表为空是正常的。** 没绑真实账号就没有持仓数据。先确认在**策略交易界面**跑、账号绑上了、类型传对了（`STOCK` / `CREDIT` / `FUTURE`）。

字段名版本间略有差异，拿不准先 `dir(obj)` 打一遍。

完整字段和示例：https://www.kimiquant.cn/problems/qmt-how-to-get-position
