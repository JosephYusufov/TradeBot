import alpaca_trade_api as tradeapi
API_KEY = "PKG1XYYRC92MYVF3B5U0"
API_SECRET = "KembGvdw3Gflnrh5UJVqiwdHS1cz1IfgIJzfbwsJ"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

alpaca = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v2') 
# account = alpaca.get_account()
# print(account)
buy = alpaca.submit_order(
    "ES",
    "1",
    "buy",
    "market",
    "day"
)

print(buy)

cancel = alpaca.cancel_order(buy.id)
