# PTrade 为什么 9:30 下单失败

开盘第一分钟委托被拒，先对这四条。

**1. 还在盘前。** 交易环境里 9:30 之前是盘前。`before_trading_start`、`run_daily(time='09:15')` 可以跑，但连续竞价还没开始，很多品种这时下单会失败。回测的 `handle_data` 从 9:31 开始，交易从 9:30 到 14:59。

**2. 限价小数位不对。** 股票两位，转债 / ETF / LOF 三位。多一位或少一位，柜台直接拒。

```python
price = round(price, 2)   # 股票
# price = round(price, 3)  # 转债 / ETF
order(security, 100, limit_price=price)
```

**3. 没传限价，快照又空。** `order()` 不传 `limit_price` 时用快照最新价。9:30 快照还没到就会失败。集合竞价后几秒再下，或自己算好限价传入。

**4. 后缀或代码不存在。** PTrade 上交所用 `.SS`，不是 QMT 的 `.SH`。

完整说明：https://www.kimiquant.cn/problems/ptrade-930-order-fail

查 `order`：https://www.kimiquant.cn/tools/api?q=order
