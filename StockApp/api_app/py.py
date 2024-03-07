# testing apis
import requests
    
# test    
# historical data using REST Apis
## json 
## csv
headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token 7eb78fa4eb950d98a130935a693d016ea738cedf'
        }
requestResponse = requests.get("https://api.tiingo.com/api/test/",
                                    headers=headers)
print(requestResponse.json())


# get historical data

symbol = "aapl"
startDate = {}

historicalResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2024-03-04& \
                                   format=csv",
                                   headers=headers)
print(historicalResponse.json())

# get todays data
currentPriceResponse = requests.get("https://api.tiingo.com/tiingo/daily/<ticker>/prices", 
                                    headers=headers)
print(currentPriceResponse.json())

# meta data for stock
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl", 
                               headers=headers)

print(requestResponse.json())

# get meta data about a stock
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl", headers=headers)
print(requestResponse.json())

# websocket for real time stream data             

from websocket import create_connection
import simplejson as json
ws = create_connection("wss://api.tiingo.com/test")

subscribe = {
                'eventName':'subscribe',
                'eventData': {
                            'authToken': '7eb78fa4eb950d98a130935a693d016ea738cedf'
                            }
                }

ws.send(json.dumps(subscribe))
for i in range(2):
    print(ws.recv())
                        
