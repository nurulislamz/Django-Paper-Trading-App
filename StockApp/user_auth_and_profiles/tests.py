# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_view
from .models import Profile

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'user_auth_and_profiles/home.html')
        
    def test_navigation_bar_functionality(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home')
    
    def test_authenticated_nav_bar(self):
        self.client.login(username='user', password='pass')
        response = self.client.get('/')
        self.assertContains(response, 'Logout')
    
# class LoginTest(TestCase):

#     def test_valid_input(self):
#         pass
    
#     def test_show_error_message(self):
#         pass
    
#     def test_submit_button(self):
#         pass
    
#     def test_redirects_after_POST(self):
#         pass
    
# class SignupTest(TestCase):

#     def test_valid_input(self):
#         pass

#     def test_validate_password(self):
#         pass
    
#     def test_duplicate_username(self):
#         pass
    
#     def test_duplicate_email(self):
#         pass
    
#     def test_submit_button(self):
#         pass
    
#     def test_redirects_after_POST(self):
#         pass
    
#     def test_deposits_saves_to_profile(self):
#         pass
    
# class ProfilePageTest(TestCase):
#     def test_edit_username_valid(self):
#         pass
    
#     def test_edit_username_invalid(self):
#         pass
      
#     def test_redirects_after_POST(self):
#         pass