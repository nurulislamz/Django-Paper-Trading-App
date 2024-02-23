"""
URL configuration for StockApp project.

"""
from django.contrib import admin
from django.urls import path, include

from user_auth_and_profiles.views import home, LoginView, SignUpForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_and_profiles.urls'), name = "user_auth"),
]