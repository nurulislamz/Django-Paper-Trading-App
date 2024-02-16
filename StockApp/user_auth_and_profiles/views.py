from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserEditForm, UpdateUserProfileForm

def home(request):
    return render(request, 'user_auth_and_profiles/home.html')

class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'user_auth_and_profiles/signup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            
            return redirect('home_page')
        else:
            return render(request, self.template_name, {'form': form})

def UserLoginView(LoginView):
    return