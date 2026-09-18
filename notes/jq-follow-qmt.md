# 聚宽策略怎么跟单到自己的 QMT（不用整段重写）

策略在聚宽模拟盘已经能下单，券商端是 QMT，又不想先整套重写时，可以先走**信号同步**：模拟盘 `order*` 照常，经 HTTPS 到本站，本机 QMT 用 `passorder` / `cancel` 执行。不代操盘、不碰券商密码。

| 路线 | 适合谁 |
| --- | --- |
| 信号同步 | 模拟盘已稳定，只想本机执行 |
| 整段迁移 | 要完全离开聚宽、长期只跑 QMT |

三步：转换页覆盖聚宽策略 → QMT「模型交易」贴执行器并运行 → 下一笔小单看「最近信号」和 QMT 日志。

和自建 Redis / 文件 / 开源 jq2qmt 比：不用自己挂服务器，不碰聚宽登录态；盘中约 15:15、盘后约 4 小时过期防隔夜补单。

工具：https://www.kimiquant.cn/tools/signal  
图文：https://www.kimiquant.cn/notes/jq-signal-qmt  
延迟实测：https://www.kimiquant.cn/notes/jq-signal-latency  
整段迁移：https://www.kimiquant.cn/problems/jq-to-qmt
