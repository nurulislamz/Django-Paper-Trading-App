from django.db import models

# Static Data
class Stock(models.Model):
    symbol = models.CharField(max_length = 5, unique = True)
    name = models.CharField(max_length = 255)
    market = models.CharField(max_length = 10)
    sector = models.CharField(max_length = 50, null = True, blank = True)
    industry = models.CharField(max_length = 255, null = True, blank = True)
    
    def __str__(self):
        return f"{self.symbol} - {self.name}"
    
# Dynamic Data
class StockPrice(models.Model):
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits = 10, decimal_place = 2)
    high = models.DecimalField(max_digits = 10, decimal_place = 2)
    low = models.DecimalField(max_digits = 10, decimal_place = 2)
    volume = models.DecimalField(max_digits = 10, decimal_place = 2)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.symbol} - {self.name}"
                