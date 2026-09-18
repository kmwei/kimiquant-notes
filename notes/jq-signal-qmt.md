# 聚宽模拟盘信号怎么接到自己的 QMT

聚宽继续跑你自己的模拟盘；本站只传下单指令；**QMT 在你自己电脑上跑**。不碰券商密码，不代操盘。

## 四步

1. 打开 [信号同步](https://www.kimiquant.cn/tools/signal) 登录（手机号验证码）。
2. 创建策略，复制 `kq_` Token（聚宽和 QMT 共用，别外传）。
3. 把策略贴进转换页。**代码只在浏览器里改**，不会上传到服务器。覆盖回聚宽后重跑模拟盘。
4. 把「QMT」整段贴进「模型交易」，选资金账号后点**运行**（`run_time` 回测不进）。

免费档约 5 秒一轮；付费档默认约 50 毫秒一轮（可自定义）。延迟实测见 [jq-signal-latency](jq-signal-latency.md)。

价格：限价 → `prType=11`；市价 → 上交所 `42` / 深交所 `47`。`cancel_order` 撤的是本机 QMT 该标的未完成单。

完整图文：https://www.kimiquant.cn/notes/jq-signal-qmt  
选型：https://www.kimiquant.cn/problems/jq-follow-qmt
