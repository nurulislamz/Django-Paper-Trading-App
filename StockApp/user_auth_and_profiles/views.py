from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserEditForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .models import Profile

def home(request):
    return render(request, 'user_auth_and_profiles/home.html')

class sign_up_view(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'user_auth_and_profiles/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(sign_up_view, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')            
            deposit = form.cleaned_data.get('deposit')
            
            user.profile.balance = deposit
            user.profile.save()
            messages.success(request, f'Account created for {username}')
            
            return redirect(to='home_page')

        return render(request, self.template_name, {'form': form})

class login_view(LoginView):   
    template_name = 'user_auth_and_profiles/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        
        if not remember_me:
            self.request.session.set_expiry(0)
            
            self.request.session.modified = True
            
        return super(login_view, self).form_valid(form)
    
class logout_view(LogoutView):
    template_name = 'user_auth_and_profiles/logout.html'

class reset_password_view(SuccessMessageMixin, PasswordResetView):
    template_name = 'user_auth_and_profiles/password_reset.html'
    email_template_name = 'user_auth_and_profiles/password_reset_email.html'
    subject_template_name = 'user_auth_and_profiles/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy("home_page")
    
@login_required
def profile_view(request):
    if request.method == 'POST':
        print(request.user)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile_page')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user_auth_and_profiles/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class change_password_view(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user_auth_and_profiles/password_reset.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home_page')