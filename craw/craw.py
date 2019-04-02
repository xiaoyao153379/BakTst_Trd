import requests
import json
import time

def craw(url):
    flag = True
    while flag:
        try:
            result = json.loads(requests.get(url,timeout = 3).text)
            flag = False
            return result
        except:
            flag = True
            time.sleep(1)


def analyze(child_conn2):
    history_id = []
    history_oder = []
    url = 'https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=usdt-btc'
    volume = 0.00
    result = craw(url)['result']
    volume += result[0]['Quantity']
    history_id.append(result[0]['Id'])
    history_oder.append(result[0])
    time.sleep(1)
    flag = True
    while flag:
        result = craw(url)['result']
        for i in result:
            if i['Id'] not in history_id:
                volume += i['Quantity']
                history_id.append(i['Id'])
                history_oder.append(i)
                child_conn2.send(i)
        time.sleep(1)
