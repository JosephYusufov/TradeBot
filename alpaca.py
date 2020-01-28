import urllib3
import json
import random
import csv
import sqlite3
ALPACA_KEY = ""
with open("credentials/alpaca_KEY.txt", 'r') as file:
    data = file.read()
    ALPHAVANTAGE_KEY = data
        
