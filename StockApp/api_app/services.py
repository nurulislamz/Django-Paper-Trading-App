import requests
from websocket import create_connection
import simplejson as json
import datetime
import asyncio 

from django.core.exceptions import FieldDoesNotExist
from django.core.validators import EMPTY_VALUES

class tiingoAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tiingo.com/tiingo/"
        self.headers = {
                        'Content-Type': 'application/json',
                        'Authorization' : 'Token' + self.apikey
                        }
        
    def __test__(self):
        headers = {
                    'Content-Type': 'application/json',
                    'Authorization' : 'Token' + self.apikey
                  }
        
        requestResponse = requests.get("https://api.tiingo.com/api/test/", headers=headers)
        print(requestResponse.json())
        
class tiingoStockAPI(tiingoAPI):
    def __init__(self, ticker):
        self.ticker = ticker
        
    async def get_historical_data(self, startDate, endDate, resampleFreq, responseFormat, columns):
        response = requests.get(f"https://api.tiingo.com/tiingo/daily/{self.ticker}/prices?startDate={startDate}&format={responseFormat}", 
                                headers=headers)
        return response.json()
    
    # get todays data
    async def get_current_price(self):
        while running:
            await asyncio.wait(30)
            response = requests.get("https://api.tiingo.com/tiingo/daily/{self.ticker}/prices", 
                                    headers=headers)
            return response.json()
        
    async def get_metadata(self):
        response = requests.get("https://api.tiingo.com/tiingo/daily/{self.ticker}", headers=headers)
        print(response.json())
        
class tiingoNewsAPI(tiingoAPI):
    def __init__(self):
        self.base_url = "https://api.tiingo.com/tiingo/news"

    async def get_latest_news(self):
        response = requests.get("https://api.tiingo.com/tiingo/news")
        return response.json()
        
    async def get_latest_news_for_tickers(self):
        response = requests.get("https://api.tiingo.com/tiingo/news?tickers=aapl,googl")
        return response.json()

    async def get_latest_news_for_countries(self):
        response = requests.get("https://api.tiingo.com/tiingo/news?tags=election,argentina")
        return response
    
    async def download_news(self):
        response = requests.get("https://api.tiingo.com/tiingo/news/bulk_download")
        return response

class tiingoCryptoAPI(self):
    def __init__(self, tickers):
        self.ticker = ticker
        
    async def get_top_of_book_data(self):
        response = requests.get("https://api.tiingo.com/tiingo/crypto/top?tickers=btcusd,fldcbtc")

    async def get_current_data(self):
        response = requests.get("https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd,fldcbtc")
        
    async def get_historical_data(self):
        response = requests.get("https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd,fldcbtc&startDate=2019-01-02&resampleFreq=5min")

    async def get_metadata_for_all_tickers(self):
        response = requests.get("https://api.tiingo.com/tiingo/crypto")

    async def get_metadata_for_specific_ticker(self):
        response = requests.get("https://api.tiingo.com/tiingo/crypto?tickers=<ticker>")

