from django.test import TestCase
from .models import Stock, StockPrice
from django.utils import timezone

class StockModelTest(TestCase):
    def test_stock_creation(self):
        stock = Stock.objects.create(symbol="AAPL", name="Apple Inc.", market = "NASDAQ")
        self.assertEqual(stock.name, "Apple Inc.")
        self.assertEqual(stock.market, "NASDAQ")
        
class StockPriceModelTest(TestCase):
    def test_stock_price_creation(self):
        stock = Stock.objects.create(symbol="AAPL", name="Apple Inc.", market = "NASDAQ")
        stock_price = StockPrice.objects.create(symbol=stock, price=150.00, high=155.00, low=149.00, volume=100000, date=timezone.now())
        self.assertEqual(stock_price.price, 150.00)
        self.assertEqual(stock_price.high, 155.00)
        self.assertEqual(stock_price.low, 149.00)
        self.assertEqual(stock_price.volume, 100000)
        self.assertEqual(stock_price.date, timezone.now())


