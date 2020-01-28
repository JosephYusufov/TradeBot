import urllib3
import json
import random
import csv
import sqlite3
ALPHAVANTAGE_KEY = ""
with open("credentials/alphavantage_KEY.txt", 'r') as file:
    data = file.read()
    ALPHAVANTAGE_KEY = data
        

class PriceData:
    """
    A class that retrieves and formats price data on a given symbol and interval. Is in object form in order
    to be passed around conveniently
    """        
    def __init__(self, symbol, interval, data):
        """
        Instantiate when given an ALREADY FORMATTED dictionary
        """
        self.symbol = symbol
        self.interval = interval
        self.data = data

        
    def __init__(self, symbol, interval):
        """
        Instantiate without any given data (The preferred way to use this class)
        """
        self.symbol = symbol
        self.interval = interval
        self.data = {}
        self.query_API()

        
    def query_API(self):
        """
        Uses the object's symbol and interval to retrieve stock price data
        """
        http = urllib3.PoolManager()
        querystring = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}&apikey={}".format(
            self.symbol, self.interval, ALPHAVANTAGE_KEY)
        
        # print(querystring)
        r = http.request('GET', querystring) 
        response = json.loads(r.data.decode('utf-8'))
        for member in response[ "Time Series ({})".format(self.interval) ]:
            self.data[member] = (response["Time Series ({})".format(self.interval)][member]["2. high"],
                                 response["Time Series ({})".format(self.interval)][member]["3. low"])

            
    def __str__(self):
        to_return = ""
        to_return += "symbol: [{}]\n".format(self.symbol)
        to_return += "interval: [{}]\n".format(self.interval)
        if not data:
            toreturn = "\t[]\n"
        else:
            to_return += "TIME                   LOW           HIGH\n"
            to_return += "-----------------------------------------\n"
            for member in self.data:
                to_return += "{}    {}    {}\n".format(member, self.data[member][0], self.data[member][1])
        return to_return

    
def fetch(symbol, interval):
    """
    Fetch (and print) price data for a company as frequently as specified by the user.

    Keyword Params:
    symbol -- must be a valid NYSE symbol
    interval -- 1min, 5min, 15min, 30min, 60min

    Return Value:
    Dictionary with Meta Data and data, as specified in the AlphaVantage docs. Not formatted, dictionary formatted exactly like the 
    API response (use PriceData.get_data() instead.)
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



# TEST CODE

AMD_5min = PriceData("AMD", "5min")
print(AMD_5min)

NVDA_1min = PriceData("NVDA", "1min")
print(NVDA_1min.data["2020-01-27 15:59:00"])
