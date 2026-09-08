# QMT 如何获取盘口

盘口是最新买卖档和最新价，不是日线 `close`。

| 需求 | 函数 | 注意 |
| --- | --- | --- |
| 最新一笔 / 盘口 | `get_full_tick` | 不能回测 |
| 推送进来再处理 | `subscribe_quote` | 回测无效，非 VIP 有订阅上限 |
| 历史 K 线 | `get_market_data_ex` | 不要拿它当「当前盘口」 |

读最新价和买一：

```python
#coding:gbk
def init(C):
    C.codes = ['600000.SH']

def handlebar(C):
    if not C.is_last_bar():
        return
    tick = C.get_full_tick(C.codes).get('600000.SH') or {}
    print(tick.get('lastPrice'), tick.get('bidPrice'))
```

买卖档缺失通常是全推没开。盘中当日日线的 `close` 会一直变，已定稿日线把 `end_time` 截到上一交易日。

完整说明：https://www.kimiquant.cn/problems/qmt-how-to-get-quote
