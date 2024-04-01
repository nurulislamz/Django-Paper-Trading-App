# testing apis
import requests

# test    
# historical data using REST Apis
## json 
## csv

from dotenv import load_dotenv, dotenv_values

api_key = '7eb78fa4eb950d98a130935a693d016ea738cedf'

from services import tiingoStockAPI

# get todays data

headers = {
            'Content-Type': 'application/json',
            'Authorization' : 'Token '+ api_key
          }

requestResponse = requests.get("https://api.tiingo.com/api/test/", headers=headers)
print(requestResponse.json())

# get todays data
ticker = "aapl"
startDate = {}

stockApi = tiingoStockAPI(api_key=api_key, ticker=ticker)
print(stockApi.get_current_price())

print(stockApi.get_current_price()['close'])

print(stockApi.get_metadata())



# get meta data about a stock
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl", headers=headers)
print(requestResponse.json())


# get historical data
# historicalResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2024-03-04& \
#                                    format=csv",
#                                    headers=headers)
# print(historicalResponse.json())

# # # get todays data
# response = requests.get(f"https://api.tiingo.com/tiingo/daily/{ticker}/prices", 
#                             headers= headers)
# print(response.json())

# # meta data for stock
# requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl", 
#                                headers=headers)

# print(requestResponse.json())



# # news data

# # For the latest news
# "https://api.tiingo.com/tiingo/news"

# # For the latest news for specific tickers
# "https://api.tiingo.com/tiingo/news?tickers=aapl,googl"

# # For the latest news for specific tags/countries/topics/tc
# "https://api.tiingo.com/tiingo/news?tags=election,argentina"

# # For a list of all the bulk download files
# "https://api.tiingo.com/tiingo/news/bulk_download"

# # To download a specific batch file
# "https://api.tiingo.com/tiingo/news/bulk_download/{id}"


# # Crypto

# # Top-of-Book Data for specific tickers
# "https://api.tiingo.com/tiingo/crypto/top?tickers=btcusd,fldcbtc"

# # Real-time (Latest) Data for specific tickers
# "https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd,fldcbtc"

# # Historical Prices
# "https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd,fldcbtc&startDate=2019-01-02&resampleFreq=5min"

# # To request meta data for all tickers, use the following REST endpoint
# "https://api.tiingo.com/tiingo/crypto"
    
# # To request meta data for a specific tickers, use the following REST endpoint
# "https://api.tiingo.com/tiingo/crypto?tickers=<ticker>"

# # To see the available fundamental metrics, use this endpoint
# "https://api.tiingo.com/tiingo/fundamentals/definitions"

# # To request historical statement data, use this endpoint
# "https://api.tiingo.com/tiingo/fundamentals/<ticker>/statements"

# # To request historical daily fundamental data, use this endpoint
# "https://api.tiingo.com/tiingo/fundamentals/<ticker>/daily"

# # To request fundamental meta data, use this endpoint
# "https://api.tiingo.com/tiingo/fundamentals/meta"


#dividends


# websocket for real time stream data             

# from websocket import create_connection
# import simplejson as json
# ws = create_connection("wss://api.tiingo.com/test")

# subscribe = {
#                 'eventName':'subscribe',
#                 'eventData': {
#                             'authToken': '7eb78fa4eb950d98a130935a693d016ea738cedf'
#                             }
#                 }

# ws.send(json.dumps(subscribe))
# for i in range(2):
#     print(ws.recv())
    
# # iex live ticker data
# ws = create_connection("wss://api.tiingo.com/iex")

# subscribe = {
#         'eventName':'subscribe',
#         'authorization':'7eb78fa4eb950d98a130935a693d016ea738cedf',
#         'eventData': {
#             'thresholdLevel': 5
#     }
# }

# ws.send(json.dumps(subscribe))
# while True:
#     print(ws.recv())
