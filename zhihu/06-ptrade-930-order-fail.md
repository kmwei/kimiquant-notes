# PTrade 一开盘就下单失败，先看这四条

9:30 第一分钟被拒，不一定是券商抽风。

1. **还在盘前。** 9:30 之前连续竞价没开始。`before_trading_start` 能跑，不代表这时能成交。回测的 `handle_data` 甚至从 9:31 才开始。
2. **限价小数位。** 股票两位，转债 / ETF 三位。多一位柜台直接拒。
3. **没传限价，快照还是空的。** `order()` 不写 `limit_price` 时吃快照最新价。开盘那几秒快照没到，委托就会失败。
4. **代码尾缀。** PTrade 上交所是 `.SS`，从 QMT 拷过来的 `.SH` 会找不到标的。

展开说明和限价示例：https://www.kimiquant.cn/problems/ptrade-930-order-fail
