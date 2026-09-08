# QMT 的 `run_time` 回测为什么不跑

这是机制，不是你写错了。

`run_time` / `schedule_run` 在**模型回测里不会执行**。回测只按 K 线驱动 `handlebar`。

| 写法 | 回测 | 实盘运行 |
| --- | --- | --- |
| `handlebar` | 可以 | 可以 |
| `subscribe_quote` | 否 | 可以 |
| `run_time` | **否** | 可以 |

要回测定时逻辑：把同样的判断写进 `handlebar`，用 `C.is_last_bar()` 或 K 线时间过滤。

```python
#coding:gbk
def init(C):
    pass

def handlebar(C):
    if not C.is_last_bar():
        return
    # 原来写在 run_time 回调里的买卖条件，挪到这里
    pass
```

盘中仍可用 `run_time` 做秒级轮询，但那条路径没有回测。

完整说明：https://www.kimiquant.cn/problems/qmt-runtime-backtest

查 `run_time`：https://www.kimiquant.cn/tools/api?q=run_time
