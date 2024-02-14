from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget = forms.TextInput(attrs={'placeholder': 'First Name',
                                                                 'class': 'form-control',
                                                                 }))

    last_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget = forms.TextInput(attrs={'placeholder': 'Last Name',
                                                                 'class': 'form-control',
                                                                 }))

    username = forms.CharField(max_length=100,
                                 required=True,
                                 widget = forms.TextInput(attrs={'placeholder': 'Username',
                                                                 'class': 'form-control',
                                                                 }))

    email = forms.CharField(max_length=100,
                                 required=True,
                                 widget = forms.TextInput(attrs={'placeholder': 'Email',
                                                                 'class': 'form-control',
                                                                 }))
    password = forms.CharField(max_length=100,
                                 required=True,
                                 widget = forms.TextInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password'
                                                                 }))

    validate_password = forms.CharField(max_length=100,
                                 required=True,
                                 widget = forms.TextInput(attrs={'placeholder': 'Confirm Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password'
                                                                 }))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'validate_password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder':'Username',
                                                             'class':'form-control'
                                                             }))

    password = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder':'Username',
                                                             'class':'form-control'
                                                             }))
    
    remember_me = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
        
class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


  
    class Meta:
        model = User
        fields = {'username', 'email'}
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile