# BakTst_Trd
> 介绍：BakTst_Trd 是我自己写的一个比特币量化交易系统。
----
## 前言

BakTst_Trd与我的另外一个项目BakTst_Org(一个量化交易的回测系统)很相似，所以诸多模块不再一一阐述。只是阐述一些不同。BakTst_Org 传送门：[传送门](https://github.com/xiaoyao153379/BakTst_Org)

---

### 不同的地方
* api模块
* craw模块
* Portfollio 模块
* main function

### api 模块
这个模块，我并没有全部写出来。只是留了个位置在那里，让它作为整个系统的框架的一部分。

它的作用很简单：

* trade：调用交易所的 api 进行交易。
* order_cancle：调用交易所的api取消部分未成交订单。

详细的，还请参考bittrex的api文档：[传送门](https://bittrex.github.io/api/v1-1)

###craw 模块
这个模块，在之前是作为单独的一个模块使用的。先运行craw模块，收集完数据后，再运行BakTst_Org分析，但是如果作为量化交易的话，爬取数据应该是实时传输过来的，所以将craw整合，作为整个项目的一个单独的模块。并且作为单独的一个进程运行，每隔一秒，爬取一次，如果有新的订单记录，将这个记录发送到主函数。

###Portfollio 模块
在BakTst_Org里，这个模块作为仓位管理模块，扮演着限制交易的角色，在BakTst_Trd里，Portfollio 模块也是起着同样的功能。不同的是，在BakTst_Org里，Portfollio，是通过一个for循环，来遍历所有的交易。在BakTst_Trd里，Portfollio 只是限制着即将到来的那笔交易。

### main function
这个模块是整个系统的中枢。首先设置一些必要的参数，比如本金，和拥有的币的数量。然后，开多进程，让craw模块去收取数据，主进程接收数据并且分析数据，以及下订单，还有，主进程也会判断一段时间内，是否有未成交的订单，然后取消它。