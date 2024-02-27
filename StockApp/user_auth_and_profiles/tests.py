from selenium import webdriver
from selenium import webdriver.commons.by import by



# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest


from lists.views import home_page
from lists.models import Item, List

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/')
        
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.endswith('</html>'))

    def test_login_and_signup_buttons(self):
        pass
    
    def test_navigation_bar_functionality(self):
        pass
    
    def test_authenticated_nav_bar(self):
        pass
    
    
class LoginTest(TestCase):

    def test_valid_input(self):
        pass
    
    def test_show_error_message(self):
        pass
    
    def test_submit_button(self):
        pass
    
    def test_redirects_after_POST(self):
        pass
    
class SignupTest(TestCase):

    def test_valid_input(self):
        pass

    def test_validate_password(self):
        pass
    
    def test_duplicate_username(self):
        pass
    
    def test_duplicate_email(self):
        pass
    
    def test_submit_button(self):
        pass
    
    def test_redirects_after_POST(self):
        pass
    
    def test_deposits_saves_to_profile(self):
        pass
    
class ProfilePageTest(TestCase):
    def test_edit_username_valid(self):
        pass
    
    def test_edit_username_invalid(self):
        pass
      
    def test_redirects_after_POST(self):
        pass