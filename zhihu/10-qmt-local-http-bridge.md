# 只有大 QMT、没有 miniQMT，外部 Python 还能怎么用

不一定非要 miniQMT。先分清你缺的是哪一样：**本机调不通接口**，还是**策略想留在别处**。

**路一：在客户端里起本机 HTTP。** 大 QMT 内置 Python 自带 tornado，不用再装框架。监听 `127.0.0.1`，路由先三个就够——健康检查、分笔、资金持仓。外部脚本用 HTTP 拿数据，研究代码继续写在你自己熟悉的 Python 里。

⚠️ 必踩的坑：有人在 `init` 里直接 `IOLoop.current().start()`。这一句会**占住线程**，`handlebar` 再也不进，表现是「桥能访问但策略日志不刷新」。正确做法是把 IOLoop 丢到后台线程，再留一句心跳日志自检。

**路二：用开源桥。** 手上已是一整套 `xtquant` 写法、想尽量不改代码，就选 [cfquant](https://github.com/95ge/cfquant)（MIT）这类项目，把大 QMT 桥成接近 miniQMT 的调用。

**路三：策略不搬，只接信号。** 策略继续在聚宽跑，只把委托指令转到本机执行。

写法和完整示例：https://www.kimiquant.cn/problems/qmt-local-http-bridge
