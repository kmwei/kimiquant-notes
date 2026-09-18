# QMT 和 PTrade 不是「哪个更好」，是四件事不一样

选错不会立刻出问题，会在**迁移的时候集中还债**。

1. **运行位置。** QMT 在本机客户端跑，关机就停；PTrade 是券商服务器托管。这决定了你的机器要不要常开。
2. **上交所尾缀。** QMT 是 `.SH`，PTrade 是 `.SS`（也可写 `.XSHG`）。互相拷代码先全局替换。
3. **字段命名毫无关联。** QMT 是 `m_nVolume` / `m_nCanUseVolume`；PTrade 是 `amount` / `enable_amount`。没有「改个后缀就能跑」这回事。
4. **环境。** QMT 内置 Python 约 3.6.8、有包白名单；PTrade 托管环境的依赖和 API 受券商限制，能做的事比本机少。

另外一个容易被忽略的：PTrade 的 `get_snapshot` 大约 **3 秒一帧**，拿它做日内高频会吃亏。

完整对照：https://www.kimiquant.cn/problems/qmt-vs-ptrade
