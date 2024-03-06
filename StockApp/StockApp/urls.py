"""
URL configuration for StockApp project.

"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_and_profiles.urls'), name = "user_auth"),
    path('stock_data/', include('stock_data_app.urls'), name="stock_data")
]