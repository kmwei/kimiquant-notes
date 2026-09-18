# 大 QMT 怎么用成 miniQMT：开源 cfquant

外部 Python 习惯 `xtquant` / miniQMT，券商端却只有**大 QMT**时，需要一层本地桥。[cfquant](https://github.com/95ge/cfquant)（MIT）就是干这个的：大 QMT 里跑入口策略，外面继续按接近 miniQMT 的写法调行情、查询和下单。

| 你卡住的点 | 做法 |
| --- | --- |
| 外部 `xtquant` 直连大 QMT 不通 | 大 QMT 加载桥接入口，外面用 `cfquant` 兼容层 |
| 要看绑定 / 通道是否在线 | 本机 Web 控制台 |
| 券商有 Python 包白名单 | 「极致模式」自包含入口脚本 |

三种模式（以官方 README 为准）：通用 / 极致 / 高级。不确定先通用。

和本站其它方案的差别：

- **要 xtquant 写法不变、接大 QMT** → 看 cfquant
- **聚宽模拟盘跟到本机 QMT** → [信号同步](https://www.kimiquant.cn/tools/signal)，不必先上 cfquant
- **只要几个对账接口** → [自建本机 HTTP 桥](https://www.kimiquant.cn/problems/qmt-local-http-bridge)

完整选型与上手：https://www.kimiquant.cn/notes/cfquant-miniqmt-bridge
