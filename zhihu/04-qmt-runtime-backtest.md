# QMT 回测里 run_time 为什么完全不跑

你在回测日志里看不到 `run_time` 回调，通常不是写错，而是**回测根本不会走这条路径**。

QMT 回测只按 K 线驱动 `handlebar`。`run_time`、`schedule_run`、`subscribe_quote` 都是盘中机制。

要回测定时逻辑：把同样的条件搬进 `handlebar`，用 `C.is_last_bar()` 或 K 线时间过滤。盘中仍可以用 `run_time` 做秒级轮询，但那条路没有回测曲线。

对照表和改法：https://www.kimiquant.cn/problems/qmt-runtime-backtest
