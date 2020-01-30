import alpaca_trade_api as tradeapi
API_KEY = "PKL38AOZCYBQTOLJQRWL"
API_SECRET = "XpoxrGiRoc8DQOWgNaRmZASmRjE1gYBGcz2/SZ4S"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

alpaca = tradeapi.REST(API_KEY, API_SECRET, api_version='v2') 
# account = alpaca.get_account()
print(alpaca.list_positions())
