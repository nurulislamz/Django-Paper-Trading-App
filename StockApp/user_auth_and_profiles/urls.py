from django.urls import path
from user_auth_and_profiles.views import UserLoginView, edit_user_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='Login Page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/', edit_user_profile, name='edit_profile')
]