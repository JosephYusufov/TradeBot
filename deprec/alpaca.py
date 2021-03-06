import urllib3
import json
import random
import csv
import sqlite3
ALPACA_KEY = ""
with open("credentials/alpaca_KEY.txt", 'r') as file:
    data = file.read()
    ALPACA_KEY = data
    
        
def buy(symbol, qty):
    """
    Buys a quantity of shares of a stock.

    Params:
    symbol -- valid NYSE symbol
    qty -- number of shares to buy
    """
    http = urllib3.PoolManager()
    querystring = "https://paper-api.alpaca.markets/v2/orders".format(
        symbol, interval, ALPHAVANTAGE_KEY)

    fields = {
        
    }
    # print(querystring)
    r = http.request('POST', querystring, fields = fields) 
    data = json.loads(r.data.decode('utf-8'))
