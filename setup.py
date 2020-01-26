import urllib3
import json
import random
import csv
import sqlite3
http = urllib3.PoolManager()
	
r = http.request( 'GET', 
	'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=NUOQ0ZH9OLWO0Y0S'
	)
r.status

MSFT = json.loads(r.data.decode('utf-8'))

# print(json.dumps(MSFT, indent=2))


for member in MSFT["Time Series (5min)"]:
	print("{}    {}    {}".format(member, MSFT["Time Series (5min)"][member]["2. high"], MSFT["Time Series (5min)"][member]["3. low"]))