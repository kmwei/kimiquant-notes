# PTrade 用 `.SS`，QMT 用 `.SH`

两边都是上交所股票，**尾缀不一样**。从教程拷代码到另一边，先全局替换，否则取数和下单都会空。

| 市场 | PTrade | QMT |
| --- | --- | --- |
| 上交所 | `600000.SS`（也可写 `.XSHG`） | `600000.SH` |
| 深交所 | `000001.SZ` | `000001.SZ` |

典型事故：

- QMT 里写 `600000.SS`：`get_full_tick` 空、废单
- PTrade 里写 `600000.SH`：`get_history` / `order` 找不到标的

完整对照和指数尾缀：https://www.kimiquant.cn/problems/ss-vs-sh

查函数：https://www.kimiquant.cn/tools/api
