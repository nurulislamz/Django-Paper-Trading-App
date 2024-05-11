from django.db import models

from django.contrib.auth.models import User
from user_auth_and_profiles.models import Profile
from stock_data_app.models import Stock

# Create your models here.
# Static Data
class Portfolios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    ticker = models.CharField(max_length = 5)
    price = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.ticker} - {self.name}"
    
class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length = 5)
    price = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.ticker} - {self.name}"
    