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
            #messages.success(request, f'searching stock: {stock_search}')
            
            StockAPI = tiingoStockAPI('7eb78fa4eb950d98a130935a693d016ea738cedf', stock_search)

            # current_stock_price = StockAPI.get_current_price()
            # historical_data = StockAPI.get_historical_data()
            # metadata = StockAPI.get_metadata()
             
            current_stock_price = {'adjClose': 171.48, 'adjHigh': 172.23, 'adjLow': 170.51, 'adjOpen': 171.75, 'adjVolume': 65672690, 'close': 171.48, 'date': '2024-03-28T00:00:00+00:00', 'divCash': 0.0, 'high': 172.23, 'low': 170.51, 'open': 171.75, 'splitFactor': 1.0, 'volume': 65672690}
            
            metadata  = {'ticker': 'AAPL', 'name': 'Apple Inc', 'description': "Apple Inc. (Apple) designs, manufactures and markets mobile communication and media devices, personal computers, and portable digital music players, and a variety of related software, services, peripherals, networking solutions, and third-party digital content and applications. The Company's products and services include iPhone, iPad, Mac, iPod, Apple TV, a portfolio of consumer and professional software applications, the iOS and OS X operating systems, iCloud, and a variety of accessory, service and support offerings. The Company also delivers digital content and applications through the iTunes Store, App StoreSM, iBookstoreSM, and Mac App Store. The Company distributes its products worldwide through its retail stores, online stores, and direct sales force, as well as through third-party cellular network carriers, wholesalers, retailers, and value-added resellers. In February 2012, the Company acquired app-search engine Chomp.", 'startDate': '1980-12-12', 'endDate': '2024-03-28', 'exchangeCode': 'NASDAQ'}
             
            historical_data = [ {'date': '2024-03-04T00:00:00.000Z', 'close': 175.1, 'high': 176.9, 'low': 173.79, 'open': 176.15, 'volume': 81510101, 'adjClose': 175.1, 'adjHigh': 176.9, 'adjLow': 173.79, 'adjOpen': 176.15, 'adjVolume': 81510101, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-05T00:00:00.000Z', 'close': 170.12, 'high': 172.04, 'low': 169.62, 'open': 170.76, 'volume': 95132355, 'adjClose': 170.12, 'adjHigh': 172.04, 'adjLow': 169.62, 'adjOpen': 170.76, 'adjVolume': 95132355, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-06T00:00:00.000Z', 'close': 169.12, 'high': 171.24, 'low': 168.68, 'open': 171.06, 'volume': 68587707, 'adjClose': 169.12, 'adjHigh': 171.24, 'adjLow': 168.68, 'adjOpen': 171.06, 'adjVolume': 68587707, 'divCash': 0.0, 'splitFactor': 1.0}, 
                                {'date': '2024-03-07T00:00:00.000Z', 'close': 169.0, 'high': 170.73, 'low': 168.49, 'open': 169.15, 'volume': 71765061, 'adjClose': 169.0, 'adjHigh': 170.73, 'adjLow': 168.49, 'adjOpen': 169.15, 'adjVolume': 71765061, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-08T00:00:00.000Z', 'close': 170.73, 'high': 173.7, 'low': 168.94, 'open': 169.0, 'volume': 76267041, 'adjClose': 170.73, 'adjHigh': 173.7, 'adjLow': 168.94, 'adjOpen': 169.0, 'adjVolume': 76267041, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-11T00:00:00.000Z', 'close': 172.75, 'high': 174.38, 'low': 172.05, 'open': 172.94, 'volume': 58929918, 'adjClose': 172.75, 'adjHigh': 174.38, 'adjLow': 172.05, 'adjOpen': 172.94, 'adjVolume': 58929918, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-12T00:00:00.000Z', 'close': 173.23, 'high': 174.03, 'low': 171.01, 'open': 173.15, 'volume': 59544927, 'adjClose': 173.23, 'adjHigh': 174.03, 'adjLow': 171.01, 'adjOpen': 173.15, 'adjVolume': 59544927, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-13T00:00:00.000Z', 'close': 171.13, 'high': 173.185, 'low': 170.76, 'open': 172.77, 'volume': 51948951, 'adjClose': 171.13, 'adjHigh': 173.185, 'adjLow': 170.76, 'adjOpen': 172.77, 'adjVolume': 51948951, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-14T00:00:00.000Z', 'close': 173.0, 'high': 174.3078, 'low': 172.05, 'open': 172.91, 'volume': 72571635, 'adjClose': 173.0, 'adjHigh': 174.3078, 'adjLow': 172.05, 'adjOpen': 172.91, 'adjVolume': 72571635, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-15T00:00:00.000Z', 'close': 172.62, 'high': 172.62, 'low': 170.285, 'open': 171.17, 'volume': 121752699, 'adjClose': 172.62, 'adjHigh': 172.62, 'adjLow': 170.285, 'adjOpen': 171.17, 'adjVolume': 121752699, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-18T00:00:00.000Z', 'close': 173.72, 'high': 177.71, 'low': 173.52, 'open': 175.57, 'volume': 75604184, 'adjClose': 173.72, 'adjHigh': 177.71, 'adjLow': 173.52, 'adjOpen': 175.57, 'adjVolume': 75604184, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-19T00:00:00.000Z', 'close': 176.08, 'high': 176.605, 'low': 173.03, 'open': 174.34, 'volume': 55215244, 'adjClose': 176.08, 'adjHigh': 176.605, 'adjLow': 173.03, 'adjOpen': 174.34, 'adjVolume': 55215244, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-20T00:00:00.000Z', 'close': 178.67, 'high': 178.67, 'low': 175.09, 'open': 175.72, 'volume': 53423102, 'adjClose': 178.67, 'adjHigh': 178.67, 'adjLow': 175.09, 'adjOpen': 175.72, 'adjVolume': 53423102, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-21T00:00:00.000Z', 'close': 171.37, 'high': 177.49, 'low': 170.84, 'open': 177.05, 'volume': 106181270, 'adjClose': 171.37, 'adjHigh': 177.49, 'adjLow': 170.84, 'adjOpen': 177.05, 'adjVolume': 106181270, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-22T00:00:00.000Z', 'close': 172.28, 'high': 173.05, 'low': 170.06, 'open': 171.76, 'volume': 
                                71160138, 'adjClose': 172.28, 'adjHigh': 173.05, 'adjLow': 170.06, 'adjOpen': 171.76, 'adjVolume': 71160138, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-25T00:00:00.000Z', 'close': 170.85, 'high': 171.94, 'low': 169.45, 'open': 170.565, 'volume': 54288328, 'adjClose': 170.85, 'adjHigh': 171.94, 'adjLow': 169.45, 'adjOpen': 170.565, 'adjVolume': 54288328, 'divCash': 0.0, 
                                'splitFactor': 1.0}, {'date': '2024-03-26T00:00:00.000Z', 'close': 169.71, 'high': 171.42, 'low': 169.58, 'open': 170.0, 'volume': 57388449, 'adjClose': 169.71, 'adjHigh': 171.42, 'adjLow': 169.58, 'adjOpen': 170.0, 'adjVolume': 57388449, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-27T00:00:00.000Z', 'close': 173.31, 'high': 173.6, 'low': 170.11, 'open': 170.41, 'volume': 60273265, 'adjClose': 173.31, 'adjHigh': 173.6, 'adjLow': 170.11, 'adjOpen': 170.41, 'adjVolume': 60273265, 'divCash': 0.0, 'splitFactor': 1.0}, {'date': '2024-03-28T00:00:00.000Z', 'close': 171.48, 'high': 172.23, 'low': 170.51, 'open': 171.75, 'volume': 65672690, 'adjClose': 171.48, 'adjHigh': 172.23, 'adjLow': 170.51, 'adjOpen': 171.75, 'adjVolume': 65672690, 'divCash': 0.0, 'splitFactor': 1.0}]
             
            context = {"form": form, 
                       "stock_search": stock_search,
                       "company_name": metadata['name'],
                       "exchange": metadata['exchangeCode'], 
                       "description": metadata['description'],
                       "current_stock_price": current_stock_price['close'],
                       "historical_data": historical_data}
            
            return render(request, self.template_name, context)
        
        