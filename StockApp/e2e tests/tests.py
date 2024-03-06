from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import unittest
import time
import os

class UserAuthTests(StaticLiveServerTestCase):

    def setUp(self):
        # self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser = webdriver.Chrome() 
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_signup(self):
        self.selenium.get(f'{self.live_server_url}/signup/')  # Update '/signup/' with your actual signup page URL
        first_name = self.selenium.find_element_by_name('first_name')  # Adjust the element selection method as needed
        last_name = self.selenium.find_element_by_name('last_name')  # Adjust the element selection method as needed
        username_input = self.selenium.find_element_by_name('username')  # Adjust the element selection method as needed
        email_input = self.selenium.find_element_by_name('email')  # Adjust the element selection method as needed
        password_input = self.selenium.find_element_by_name('password1')  # Adjust the element selection method as needed
        confirm_password_input = self.selenium.find_element_by_name('password2')  # Adjust the element selection method as needed

        username_input.send_keys('testuser')
        email_input.send_keys('testuser@example.com')
        password_input.send_keys('s3cr3tP@ssword')
        confirm_password_input.send_keys('s3cr3tP@ssword')
        confirm_password_input.send_keys(Keys.RETURN)
        
        # write assertions here
        
    
    def test_invalid_signup(self):
        # Assuming the user 'testuser' with password 's3cr3tP@ssword' already exists
        self.selenium.get(f'{self.live_server_url}/login/')  # Update '/login/' with your actual login page URL
        username_input = self.selenium.find_element_by_name('username')  # Adjust the element selection method as needed
        password_input = self.selenium.find_element_by_name('password')  # Adjust the element selection method as needed

        username_input.send_keys('testuser')
        password_input.send_keys('s3cr3tP@ssword')
        password_input.send_keys(Keys.RETURN)

        # Add assertions here to verify login success, such as checking for a specific success message or being redirected to a dashboard page