# QMT 没有单独成交回调时怎么查单

`passorder` 成功只代表委托发出去了，不代表成交。盘中要自己查。

用 `get_trade_detail_data(账号, 账号类型, 数据类型)`：

- `ORDER`：委托状态、已成数量
- `DEAL`：成交明细
- `POSITION`：持仓
- `ACCOUNT`：资金

股票账号类型是 `STOCK`，期货 `FUTURE`，两融 `CREDIT`。下单时如果带了 `strategyName`，查询时用同一个名字，避免把自己和其他策略的单混在一起。

另外：不要把已报数量塞进 `ContextInfo`。盘中逐 K 回退时它会回到上一根结束状态，长期状态用普通全局对象存。

写法示例：https://www.kimiquant.cn/problems/qmt-order-callback
