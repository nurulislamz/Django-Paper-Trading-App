from django.urls import path
from .views import home, sign_up_view, login_view #UserEditForm
from django.contrib.auth.views import LogoutView
from .forms import LoginForm

urlpatterns = [
    path('', home, name='home_page'),
    path('signup/', sign_up_view.as_view(), name='sign_up_page'),
    path('login/', login_view.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(template_name='user_auth_and_profiles/logout.html'), name='logout_page'),
    # path('edit_profile/', UserEditForm, name='edit_profile')
]