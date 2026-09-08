# QMT 的 get_full_tick 为什么是空的

盘中打印 `get_full_tick`，得到 `{}` 或缺买卖档，按这个顺序排：

1. 你是不是在**回测**里调它？这个函数只给实盘 / 运行模式。回测请用 `get_market_data_ex`，或直接读 `handlebar` 的 K 线。
2. 客户端**全推**开了没有？没开全推时，`lastPrice` 可能还有，买卖档经常缺。
3. 代码是不是写成了 PTrade 的 `600000.SS`？QMT 上交所必须是 `.SH`。
4. 用了 `subscribe_quote` 的，看有没有超过非 VIP 订阅上限。

一段最小自检代码、日志位置和手册锚点在：

https://www.kimiquant.cn/problems/qmt-no-realtime-tick

直接查函数：https://www.kimiquant.cn/tools/api?q=get_full_tick
