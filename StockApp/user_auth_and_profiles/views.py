from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import UserEditForm, UserProfileForm

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'user_auth_and_profiles/login.html'
    
def edit_user_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user, data = request.POST)
        profile_form = UserProfileForm(instance = request.user.userprofile, data = request.POST, files = request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirect to a new URL:
            return redirect('profile_view')
        
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
            
    return render(request, 'user_auth/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})