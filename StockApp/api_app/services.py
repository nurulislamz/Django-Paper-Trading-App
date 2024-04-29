import requests
from websocket import create_connection
import simplejson as json
import datetime as dt
import asyncio 

from django.core.exceptions import FieldDoesNotExist
from django.core.validators import EMPTY_VALUES

class tiingoAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tiingo.com/tiingo/"
        self.headers = {
                        'Content-Type': 'application/json',
                        'Authorization' : 'Token ' + self.api_key
                        }
        
    def __test__(self):
        headers = {
                    'Content-Type': 'application/json',
                    'Authorization' : 'Token ' + self.api_key
                  }
        
        requestResponse = requests.get("https://api.tiingo.com/api/test/", headers=headers)
        print(requestResponse.json())
        
class tiingoStockAPI(tiingoAPI):
    def __init__(self, api_key, ticker):
        super().__init__(api_key)
        self.ticker = ticker
        
    # get todays data
    def get_current_price(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/daily/{self.ticker}/prices", 
                                    headers=self.headers)
        return response.json()
        
    async def get_historical_data(self, **kwargs):
        default_date = dt.datetime.today() - dt.timedelta(days=30)
        response = await requests.get(f"https://api.tiingo.com/tiingo/daily/{self.ticker}/prices?startDate={default_date}", 
                                headers=self.headers)
        return response.json()[0]
        
    def get_metadata(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/daily/{self.ticker}", headers=self.headers)
        return response.json()
    
class tiingoNewsAPI(tiingoAPI):
    def __init__(self):
        self.base_url = "https://api.tiingo.com/tiingo/news"

    async def get_latest_news(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/news")
        return response.json()[0]
        
    async def get_latest_news_for_tickers(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/news?tickers=aapl,googl")
        return response.json()[0]

    async def get_latest_news_for_countries(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/news?tags=election,argentina")
        return response.json()[0]
    
    async def download_news(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/news/bulk_download")
        return response

class tiingoCryptoAPI(tiingoAPI):
    def __init__(self, tickers):
        self.ticker = ticker
        
    async def get_top_of_book_data(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/crypto/top?tickers=btcusd,fldcbtc")

    async def get_current_data(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd,fldcbtc")
        
    async def get_historical_data(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd,fldcbtc&startDate=2019-01-02&resampleFreq=5min")

    async def get_metadata_for_all_tickers(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/crypto")

    async def get_metadata_for_specific_ticker(self):
        response = requests.get(f"https://api.tiingo.com/tiingo/crypto?tickers=<ticker>")

class tiingoWebSocketAPI:
    pass