from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm, UserEditForm, UpdateUserForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'stock_data_app/search.html')