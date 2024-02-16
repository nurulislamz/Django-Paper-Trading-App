from django.urls import path
from .views import home, SignUpView #UserLoginView, UserEditForm
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home_page'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    # path('login/', UserLoginView.as_view(), name='Login Page'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('edit_profile/', UserEditForm, name='edit_profile')
]