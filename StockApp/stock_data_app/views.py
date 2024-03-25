from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import StockSearch
from api_app.services import tiingoStockAPI


# Create your views here.
class search_view(View):
    form_class = StockSearch
    initial = {"key": "value"}
    template_name = "stock_data_app/search.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            stock_search = form.cleaned_data.get('stock_search')
            messages.success(request, f'searching stock: {stock_search}')
            
            return render(request, self.template_name, {"form": form, "stock_search": stock_search})
        