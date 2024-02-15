from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserEditForm, UpdateUserProfileForm

def home(request):
    return render(request, 'user_auth_and_profiles/home.html')

# class SignUpView(View):
#     form_class = SignUpView
#     initial = {'key': 'value'}
#     template_name = 'users/register.html'
    
#     def dispatch(self, request, *args, **kwargs):
#         # will redirect to the home page if a user tries to access the register page while logged in
#         if request.user.is_authenticated:
#             return redirect(to='/')

#         # else process dispatch as it otherwise normally would
#         return super(RegisterView, self).dispatch(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')

#             return redirect(to='login')

#         return render(request, self.template_name, {'form': form})

# class UserLoginView(LoginView):
#     template_name = 'user_auth_and_profiles/login.html'
    
#     def edit_user_profile(request):
#         if request.method == 'POST':
#             user_form = UserEditForm(instance = request.user, data = request.POST)
#             profile_form = UpdateUserProfileForm(instance = request.user.userprofile, data = request.POST, files = request.FILES)
            
#             if user_form.is_valid() and profile_form.is_valid():
#                 user_form.save()
#                 profile_form.save()
#                 # Redirect to a new URL:
#                 return redirect('profile_view')
            
#         else:
#             user_form = UserEditForm(instance=request.user)
#             profile_form = UserProfileForm(instance=request.user.userprofile)
                
#         return render(request, 'user_auth/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})