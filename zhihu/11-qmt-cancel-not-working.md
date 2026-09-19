# QMT 撤单撤不掉：`cancel` 返回 `True` 不等于撤成了

`cancel(orderId, accountId, accountType, C)` 返回 `bool`，PTrade 的 `cancel_order()` 返回 `None`。

**这两个返回值都只表示「撤单请求发出去了」，不表示柜台已经撤单。** 撤完必须**再查一次委托状态**，而不是看返回值。

## 三种撤不掉，成因完全不同

1. **这笔单本来就不该撤。** 已全成、部成、或被拒的单，再发撤单柜台直接拒。所以撤之前要**按状态过滤**，别把委托列表整个丢进去撤一遍。
2. **`accountType` 填错。** 必须和开户类型一致：股票 `STOCK`、两融 `CREDIT`、期货 `FUTURE`。填错返回 `False`，而且**没有任何报错提示**，最容易被当成「接口坏了」。
3. **在编辑器里点运行。** 这种场景常常拿不到真实委托号，发出去的撤单在语义上就是无意义的。必须在**实盘运行**里验。

## 写法：先查单，再撤

```python
orders = get_trade_detail_data(acc, 'STOCK', 'ORDER') or []
for o in orders:
    oid = getattr(o, 'm_strOrderSysID', '') or getattr(o, 'm_strOrderID', '')
    traded = int(getattr(o, 'm_nVolumeTraded', 0) or 0)
    total = int(getattr(o, 'm_nVolumeTotalOriginal', 0) or 0)
    if not oid or (total > 0 and traded >= total):
        continue
    cancel(oid, acc, 'STOCK', C)
```

委托号用 `m_strOrderSysID`，和成交记录里是同一个字段名；版本间可能不同，先 `dir(obj)` 打一遍再写。

⚠️ PTrade 的**回测日终会自动取消未完成单**，和实盘行为不一样 —— 撤单逻辑在回测里测不出真实表现。

完整说明：https://www.kimiquant.cn/notes/cancel
