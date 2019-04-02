import json
from pandas import DataFrame
from Feed.Feed import Feed
from multiprocessing import  Manager,Pool,Pipe
from craw.craw import analyze
from api.api import order_cancle
import requests
import time

def get_price(url):
    flag = True
    while flag:
        try:
            result = json.loads(requests.get(url,timeout = 3).text)['result']['Last']
            flag = False
            return result
        except:
            flag = True




if __name__ == '__main__':
    url = 'https://api.bittrex.com/api/v1.1/public/getticker?market=USDT-BTC'
    Price = get_price(url)
    time.sleep(1)
    coin_number = 20  # 仓位拥有币数
    principal = 1000000  # 本金
    init = coin_number * Price + principal
    print('init: ' + str( init ))
    histor_oder = []
    parent_conn2, child_conn2 = Pipe()
    pool = Pool(processes=2)
    pool.apply_async(func=analyze, args=(child_conn2,))
    time = 0
    while True:
        kk = parent_conn2.recv()
        histor_oder.append(kk)
        if(len(histor_oder)>500):
            for i in range(10):
                histor_oder.pop(index=i)
        if(len(histor_oder)>100):
            col = ['Id', 'TimeStamp', 'Quantity', 'Price', 'Total', 'FillType', 'OrderType', 'Uuid']
            data_frame = DataFrame(columns=col)
            for i in histor_oder:
                data_frame = data_frame.append(i, ignore_index=True)
            feed = Feed(data_frame, coin_number, principal)
            msg = feed.send_data()
            print(msg)
            coin_number = msg['coin_number']
            principal = msg['principal']
            Price = msg['Price']
            print('Profit or loss: ' + str(coin_number * Price + principal - init))
            time += 1
            if(time == 120):
                order_cancle()
    parent_conn2.close()
    pool.close()
    pool.join()




