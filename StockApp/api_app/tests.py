from django.test import TestCase
from django.urls import reverse
import unittest
from unittest.mock import patch, MagicMock
import requests
from api_app.services import tiingoStockAPI

# Create your tests here.
class TiingoStockApiTest(TestCase):
    def setUp(self):
        self.api_key = '7eb78fa4eb950d98a130935a693d016ea738cedf'
        self.ticker = 'AAPL'
        self.api = tiingoStockAPI(api_key=self.api_key, ticker=self.ticker)
      
    def test_get_current_price(self):
        response = self.api.get_current_price()
        
        required_keys = ['close', 'volume', 'date']
        self.assertTrue(all(key in response for key in required_keys))
        
    def test_get_historical_data(self):
        pass
    
    def test_metadata(self):
        response = self.api.get_metadata()
        
        required_keys = ['description']
        self.assertTrue(all(key in response for key in required_keys))        

    # @patch('requests.get')
    # def test_get_current_price(self, mock_get):
    #     mock_response = MagicMock()
    #     mock_response.json.return_value = {
    #         'adjClose': 173.31, 'adjHigh': 173.6, 'adjLow': 170.11, 'adjOpen': 170.41, 
    #         'adjVolume': 58623507, 'close': 173.31, 'date': '2024-03-27T00:00:00+00:00', 
    #         'divCash': 0.0, 'high': 173.6, 'low': 170.11, 'open': 170.41, 'splitFactor': 1.0, 
    #         'volume': 58623507}
    #     mock_get.return_value = mock_response
        
    #     response = self.api.get_current_price()
    #     self.assertEqual(response, {'data' : 'current price data'})
        
    #     mock_get.assert_called_once_with(
    #     f"https://api.tiingo.com/tiingo/daily/{self.ticker}/prices",
    #     headers=self.api.headers
    #     )                
        
    # # @patch('request.get')
    # # def test_get_historical_data(self, mock_get):
    # #     mock_response = MagicMock()
    # #     mock_response.json.return_value = {'data': 'some historical data'}
    # #     mock_get.return_value = mock_response
            

            