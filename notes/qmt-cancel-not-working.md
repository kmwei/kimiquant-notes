# 撤单撤不掉：先查单号再撤

QMT 的 `cancel(orderId, accountId, accountType, C)` 返回 `bool`，PTrade 的 `cancel_order()` 返回 `None`。

**这两个返回值都只表示「撤单请求发出去了」，不表示柜台已经撤成。** 撤完要再查一次委托状态，而不是看返回值。

## 三种撤不掉，成因完全不同

### 1. 这笔单本来就不该撤

已经全部成交、部分成交、或者已经被柜台拒掉的单，再发撤单，柜台会直接拒绝。这不是 bug，是规则。所以撤之前必须先**按状态过滤**，而不是把所有委托都丢进去撤一遍。

### 2. 账号类型填错

`accountType` 必须和开户类型一致：股票 `STOCK`，两融 `CREDIT`，期货 `FUTURE`。填错返回值就是 `False`，而且不会有任何报错提示，很容易被当成「接口有问题」。

### 3. 编辑器里点运行，根本没有真实委托号

在 QMT 编辑器里直接点运行，很多时候拿不到真实的委托号，此时发出去的撤单**在语义上就是无意义的**。必须在**实盘运行**里验。

## 写法：先查单，再撤

```python
#coding:gbk
def init(C):
    C.acc = '你的资金账号'
    C.acct_type = 'STOCK'

def handlebar(C):
    if not C.is_last_bar():
        return
    orders = get_trade_detail_data(C.acc, C.acct_type, 'ORDER') or []
    for o in orders:
        oid = getattr(o, 'm_strOrderSysID', '') or getattr(o, 'm_strOrderID', '')
        traded = int(getattr(o, 'm_nVolumeTraded', 0) or 0)
        total = int(getattr(o, 'm_nVolumeTotalOriginal', 0) or 0)
        print('order', oid, 'traded', traded, '/', total)
        if not oid:
            continue
        if total > 0 and traded >= total:
            continue          # 已经全成，撤也没用
        print('cancel', oid, cancel(oid, C.acc, C.acct_type, C))
```

PTrade 那边结构不同，用 `get_orders()` 拿 id，撤完再用 `get_order(id)` 复查：

```python
def handle_data(context, data):
    bag = get_orders() or {}
    for oid, o in bag.items():
        st = str(getattr(o, 'status', '')).lower()
        if 'fill' in st or 'cancel' in st or 'reject' in st:
            continue
        cancel_order(oid)
        log.info('after cancel %s', get_order(oid))
```

## 两个字段坑

- 委托号用 `m_strOrderSysID`，和成交记录里是同一个字段名。**不同版本字段可能不同，先 `dir(obj)` 打印一遍再写**，别照抄网上的旧字段名。
- PTrade 的**回测日终会自动取消未完成单**，和实盘行为不一样。回测里测不出撤单逻辑的真实表现。

## 自查顺序

1. 先确认这笔委托的**当前状态**（未报、部成、已成、已撤、废单）
2. 确认 `accountType` 和开户类型一致
3. 确认是在**实盘运行**里，而不是编辑器点运行
4. 撤完**再查一次**，别信返回值

完整说明：https://www.kimiquant.cn/notes/cancel

查函数：https://www.kimiquant.cn/tools/api?q=cancel
