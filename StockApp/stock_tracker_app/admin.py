from django.contrib import admin
from .models import Portfolios, Transactions

# Register your models here.
admin.site.register(Portfolios)
admin.site.register(Transactions)