from django import forms
from .models import Stock, StockPrice

class StockSearchForm(forms.Form):
    # fields we want to include and customize in our form
    stock_search = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Stock Search',
                                                               'class': 'form-control rounded',
                                                               'aria-label': 'Search',
                                                               'aria-describedby': 'search-addon',
                                                               }))
    
    class Meta:
        model = Stock
        fields = ['stock_name']

class StockOrderForm(forms.Form):
    quantity = forms.IntegerField(required=True, 
                                   widget=forms.NumberInput(attrs={'placeholder': 'Stock Buy',
                                                                    'class': 'form-control rounded',
                                                                    'aria-label': 'Stock Buy',
                                                                    'aria-describedby': 'stock-buy',
                                                                    }))