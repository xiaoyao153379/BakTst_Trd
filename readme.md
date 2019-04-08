# BakTst_Trd
中文readme：[传送门](https://github.com/xiaoyao153379/BakTst_Trd/blob/master/readme_chinese.md)
> Introduction: BakTst_Trd is a quantitative trading system of bitcoin.
----

## preface

BakTst_Trd is similar to my other project named BakTst_Org (a backtesting system for quantitative transactions), so I just explain some differences. The address of BakTst_Org: [BakTst_Org](https://github.com/xiaoyao153379/BakTst_Org)

---

![mind](https://github.com/xiaoyao153379/BakTst_Trd/blob/master/picture/m1.png?raw=true "result")

### Differences
* api module
* craw module
* Portfollio module
* main function

### api module
I have not completed this module, and I just used it to take up a place as a part of the framework.

Its function is very simple, and it includes these parts：

* trade：It is used to call the exchange's api to trade.
* order_cancle：It is used to call the exchange's api to cancel order.

You can refer to the api of bittrex to check details：[address of API](https://bittrex.github.io/api/v1-1)

### craw module
This module was previously used as a separate module to get data. Only, after it collected the data, then you can run BakTst_Org to analyze it. But the data should be transmitted in real time, if we made a quantitative trading system. So I integrate the craw module into BakTst_Trd, and it is a separate process. It will crawl data once every second, and if it crawl a new data of order, it will send the data to main function.

### Portfollio module
In BakTst_Org, this module plays a role that limits position. In BakTst_Trd, this module also plays the same function. But there is also a difference. In BakTst_Org, this module traverses all transactions by using a for loop. In BakTst_Trd, this module only limits the upcoming deal. 

### main function
This module is the soul of the entire system. Firstly, you should set some parameters such as principal, and the number of BTC. Then it will use craw module to get data, and the main process will receive the data and analyze it. Besides, main function will also judge the order that has not been completed to cancel it.

### Result graph
![result](https://github.com/xiaoyao153379/BakTst_Trd/blob/master/picture/k.jpg?raw=true "result")