from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserEditForm, UpdateProfileForm
from django.contrib.auth.views import LoginView

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
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='home_page')

        return render(request, self.template_name, {'form': form})

class login_view(LoginView):   
    template_name = 'user_auth_and_profiles/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True,
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        
        if not remember_me:
            self.request.session.set_expiry(0)
            
            self.request.session.modified = True
            
        return super(login_view, self).form_valid(form)
    