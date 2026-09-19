# 下单返回了但没成交：先分清「没委托」还是「没成交」

看到「没成交」就去改策略逻辑，是最常见的绕远路。

第一步应该是**查委托列表里到底有没有这笔单**：

- 委托列表里**没有**这笔单 → 问题在下单之前（代码没执行到、参数被拒、账号或后缀不对）
- 委托列表里**有**这笔单 → 问题在撮合环节（价格、时段、涨跌停、停牌、资金或持仓不足）

这两条路的排查方向完全不同。

## 返回值不是委托确认

下单函数的返回值**只表示请求被客户端接受，或者给出了错误码**。它不是委托确认，更不是成交确认。

废单、部成、拒单，走的都是**委托状态**这条路，不是「函数没返回」。所以要判断真实结果，必须去看委托状态。

## 最小对账

```python
#coding:gbk
def init(C):
    C.set_account(account)

def order_callback(C, orderInfo):
    print('order', getattr(orderInfo, 'm_strInstrumentID', ''),
          getattr(orderInfo, 'm_nOrderStatus', ''),
          getattr(orderInfo, 'm_nVolumeTraded', 0))

def deal_callback(C, dealInfo):
    print('deal', getattr(dealInfo, 'm_strInstrumentID', ''),
          getattr(dealInfo, 'm_nVolume', 0),
          getattr(dealInfo, 'm_dPrice', 0))
```

回测、研究模式常常没有真实主推。要在**实盘运行**里验；对账再用 `get_trade_detail_data(account, 'STOCK', 'DEAL')`。

## 委托有了但不成交，通常是这四类

1. **价格**：限价单挂在了成交不了的位置，最常见的一种。
2. **时段**：集合竞价、非连续竞价时段，委托状态和预期不同。
3. **涨跌停 / 停牌**：一字板或停牌，挂了也是排队或废单。
4. **资金或持仓不足**：保证金、可用资金、可卖数量，任何一个不够都会被拒。

前两类是策略参数问题，后两类是账户状态问题。看委托的**状态字段**能直接区分。

## 顺手排除的低级坑

| 检查 | 说明 |
| --- | --- |
| 后缀 | 上交所用 `.SH`，不是 `.XSHG` |
| 账号 | `init` 里 `set_account`；交易界面注入的 `account` |
| 枚举 | `opType` / `prType` 别凭记忆写 |
| 时段 | 集合竞价、涨跌停、停牌会废单或不成交 |

完整说明：https://www.kimiquant.cn/problems/qmt-passorder-not-filled

委托回调怎么写：https://www.kimiquant.cn/problems/qmt-order-callback
