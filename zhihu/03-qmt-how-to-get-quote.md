# QMT 取盘口：别拿日线 close 当最新价

「盘口」是最新买卖档和最新价。日线 `close` 在盘中会一直变，那不是收盘价，更不是买一卖一。

三种取数不要混：

- 现在这一笔：`get_full_tick`
- 推送进来再处理：`subscribe_quote`（回测不跑）
- 历史 K / 均线：`get_market_data_ex`

买卖档缺失，多半是全推没开，不是函数废了。已定稿的日线，把 `end_time` 截到上一交易日。

示例和字段说明：https://www.kimiquant.cn/problems/qmt-how-to-get-quote
