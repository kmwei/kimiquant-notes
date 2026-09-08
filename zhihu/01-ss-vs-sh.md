# 从 PTrade 拷到 QMT，先换股票代码尾缀

很多人把 PTrade 策略直接贴进 QMT，取数是空的，下单是废单。第一反应是函数写错了，其实经常是**上交所尾缀不一样**。

- PTrade：`600000.SS`（全称还可以写 `.XSHG`）
- QMT：`600000.SH`
- 深交所两边都是 `.SZ`，这一项不用改

对照着搜一下 `.SS` / `.SH` / `.XSHG`，按目标平台整文件替换，不要混在同一个策略里。

指数、行业代码在 PTrade 里还有 `.XBHS` 一类，和股票不是同一套。完整表和事故例子写在这里：

https://www.kimiquant.cn/problems/ss-vs-sh

函数名不确定就查：https://www.kimiquant.cn/tools/api
