# QMT 委托回调怎么写

`passorder` 返回不等于成交。盘中要自己查委托和成交，常用 `get_trade_detail_data`：

```text
get_trade_detail_data(accountID, strAccountType, strDatatype)
```

`strDatatype`：`ORDER` 委托，`DEAL` 成交，`POSITION` 持仓，`ACCOUNT` 资金。下单时如果传了 `strategyName`，查询时带同一个名字，只拿本策略的单。

```python
#coding:gbk
def init(C):
    C.acc = '你的资金账号'

def handlebar(C):
    if not C.is_last_bar():
        return
    orders = get_trade_detail_data(C.acc, 'STOCK', 'ORDER')
    deals = get_trade_detail_data(C.acc, 'STOCK', 'DEAL')
    print(len(orders), len(deals))
```

期货账号类型用 `'FUTURE'`，两融用 `'CREDIT'`。不要用 `ContextInfo` 存长期状态，盘中逐 K 会回滚。

完整说明：https://www.kimiquant.cn/problems/qmt-order-callback

查函数：https://www.kimiquant.cn/tools/api?q=get_trade_detail_data
