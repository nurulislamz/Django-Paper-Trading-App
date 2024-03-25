# Create your tests here.
from django.urls import resolve
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .views import home_view
from .models import Profile

class NavigationBarTestCase(TestCase):
    def test_navigation_bar_loaded(self):
        response = self.client.get('/')
        self.assertContains(response, 'navbar')
    
    def test_navigation_links_for_unauthenticated_user(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, 'Home')
    
    def test_navigation_links_for_authenticated_user(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, 'Profile')


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'user_auth_and_profiles/home.html')
    
class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.login_url = reverse('login_page')  # Replace 'login' with the actual name of your login URL
    
    def test_valid_input(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, reverse('home_page'))  # Replace 'expected_url' with the URL you expect to redirect to after login

    # Not working
    # def test_show_error_message(self):
    #     response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpass'})
    #     self.assertFormError(response, 'form', 'user', 'Invalid username or password')  # Adjust the error message to match what your form returns
    
    # Not working
    # def test_submit_button(self):
    #     response = self.client.get(self.login_url)
    #     self.assertContains(response, '<button"')  # Check for the submit button in the form
    
    def test_redirects_after_POST(self):
        response = self.client.post(self.login_url, data = {'username': 'testuser', 'password': '12345'}, follow=True)
        self.assertRedirects(response, '/')  # Replace 'expected_url' with the URL you expect to redirect to after login
    
    # requires BeautifulSoup to parse through html and find the correct link
    def test_redirects_signup_link(self):
        pass
    
    def test_forgotten_password(self):
        pass
    
class SignupTest(TestCase):

    def setUp(self):
        self.signup_url = reverse('signup_page')
    
    def test_valid_input(self):
        response = self.client.post(self.signup_url, data={
            'first_name': 'testName',
            'last_name': 'testName',
            'username': 'testUsername',
            'email': 'test@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
            'deposit': '10000'
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, expected_url = reverse('home_page'))
        
    def test_validate_password(self):
        response = self.client.post(self.signup_url, data={
            'first_name': 'testName',
            'last_name': 'testName',
            'username': 'testUsername',
            'email': 'test@example.com',
            'password1': '123',
            'password2': '123',
            'deposit': '10000'
        })
        self.assertIn('password2', response.context['form'].errors)
    
    def test_duplicate_username(self):
        User.objects.create_user('existingUser', 'existingUser@example.com', 'complex_password123')
        response = self.client.post(self.signup_url, data={
            'first_name': 'testName',
            'last_name': 'testName',
            'username': 'existingUser',
            'email': 'test@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
            'deposit': '10000'
        })
        self.assertIn('username', response.context['form'].errors)
    
    # supports multiple emails currently -  need to add a new authenticator to stop it
    # def test_duplicate_email(self):
    #     User.objects.create_user('user4', 'existingUser@example.com', 'complex_password123')
    #     response = self.client.post(self.signup_url, data={
    #         'first_name': 'testName',
    #         'last_name': 'testName',
    #         'username': 'testUser4',
    #         'email': 'existingUser@example.com',
    #         'password1': 'complex_password123',
    #         'password2': 'complex_password123',
    #         'deposit': '10000'
    #     })
    #     self.assertIn('username', response.context['form'].errors)
            
    # def test_submit_button(self):
    #     self.client.get(self.signup_url)
    #     self.assertContains(response, '<button type="submit"', html= True)
    
    def test_redirects_after_POST(self):
        response = self.client.post(self.signup_url, data={
            'first_name': 'testName',
            'last_name': 'testName',
            'username': 'testUsername',
            'email': 'test@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
            'deposit': '10000'
        })
        self.assertRedirects(response, expected_url = reverse("home_page"))
            
    def test_deposits_saves_to_profile(self):
        response = self.client.post(self.signup_url, data={
            'first_name': 'testName',
            'last_name': 'testName',
            'username': 'testUsername',
            'email': 'test@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
            'deposit': '10000'
        })
        user = User.objects.get(username='testUsername')
        self.assertEqual(user.profile.balance, 10000.00)
            
class ProfilePageTest(TestCase):
    def setUp(self):
        self.profile_url = reverse('profile_page')
    
    def test_edit_username_valid(self):
        pass
    
    def test_edit_username_invalid(self):
        pass
      
    def test_redirects_after_POST(self):
        pass
    
    