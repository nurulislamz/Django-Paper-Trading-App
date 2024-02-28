from django.urls import path
from .views import home_view, sign_up_view, login_view, logout_view, profile_view, reset_password_view, change_password_view #UserEditForm
from django.contrib.auth.views import PasswordResetConfirmView, LogoutView

urlpatterns = [
    path('', home_view, name='home_page'),
    path('signup/', sign_up_view.as_view(), name='sign_up_page'),
    path('login/', login_view.as_view(), name='login_page'),
    path('logout/', logout_view.as_view(), name='logout_page'),
    path('profile/', profile_view, name='profile_page'),
    path('password_reset/', reset_password_view.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user_auth_and_profils/password_reset_confirm.html'),name='password_reset_confirm'),    
    path('password-change/', change_password_view.as_view(), name='password_change'),
    # path('edit_profile/', UserEditForm, name='edit_profile')
]