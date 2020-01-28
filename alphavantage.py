import urllib3
import json
import random
import csv
import sqlite3
ALPHAVANTAGE_KEY = ""
with open("credentials/alphavantage_KEY.txt", 'r') as file:
    data = file.read()
    ALPHAVANTAGE_KEY = data
        

def fetch(symbol, interval):
    """
    Fetch price data for a company as frequently as specified by the user

    Keyword Params:
    symbol -- must be a valid NYSE symbol
    interval -- 1min, 5min, 15min, 30min, 60min

    Return Value:
    Dictionary with Meta Data and data, as specified in the AlphaVantage docs
    """
    
    http = urllib3.PoolManager()
    querystring = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}&apikey={}".format(
        symbol, interval, ALPHAVANTAGE_KEY)
    
    # print(querystring)
    r = http.request('GET', querystring) 
    data = json.loads(r.data.decode('utf-8'))
    print("TIME                   LOW           HIGH")
    print("-----------------------------------------")
    for member in data[ "Time Series ({})".format(interval) ]:
        print("{}    {}    {}".format(member, data["Time Series ({})".format(interval)][member]["2. high"], data["Time Series ({})".format(interval)][member]["3. low"]))

    return data

fetch("AMD", "1min")
