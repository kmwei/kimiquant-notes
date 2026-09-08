# QMT 为什么获取不到实时行情

`get_full_tick` 返回空 dict、缺买卖档，或盘中像没推，先对这四条：

1. **写在回测里**。`get_full_tick` 只给实盘 / 运行模式。回测用 `get_market_data_ex` 或 `handlebar` 上的 K 线。
2. **全推档位没开**。客户端没开对应档位，买卖盘字段会缺。先读 `lastPrice`，或找营业部开全推。
3. **代码后缀错了**。QMT 上交所用 `.SH`，不要写成 PTrade 的 `.SS`。
4. **订阅数量超了**。`subscribe_quote` 非 VIP 有上限，超了后面的合约没有推送。

最小自检：

```python
#coding:gbk
def init(C):
    C.stock_list = ['600000.SH']

def handlebar(C):
    if not C.is_last_bar():
        return
    print(C.get_full_tick(C.stock_list))
```

日志在安装目录 `userdata/log`。打印仍是 `{}`，先看客户端行情是否在跳。

完整说明：https://www.kimiquant.cn/problems/qmt-no-realtime-tick

查 `get_full_tick`：https://www.kimiquant.cn/tools/api?q=get_full_tick
