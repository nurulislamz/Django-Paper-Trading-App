from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime as dt


# Static Data
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length = 5, unique = True)
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 10)
    
    def __str__(self):
        return f"{self.ticker} - {self.name}"
    
# Dynamic Data
class StockPrice(models.Model):
    ticker = models.CharField(max_length = 5, unique = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateTimeField(default=dt.datetime.now())
            