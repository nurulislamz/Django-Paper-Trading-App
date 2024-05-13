from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Portfolios
from api_app.services import tiingoStockAPI

import logging
import json

# Create your views here.
class portfolio_view(View):
    initial = {"key": "value"}
    template_name = "stock_tracker_app/portfolio.html"

    def get(self, request):
        return render(request, self.template_name)

    
