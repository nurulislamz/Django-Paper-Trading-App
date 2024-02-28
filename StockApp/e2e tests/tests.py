from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import unittest
import time
import os

class SignUpTests(StaticLiveServerTestCase):

    def setUp(self):
        # self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser = webdriver.Chrome() 
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_valid_signup(self):
        pass
    
    def test_invalid_signup(self):
        pass
    
    def test_data_persistence_after_signup(self):
        pass
    
    def test_redirect_after_signup(self):
        pass


class LoginTests(StaticLiveServerTestCase):
    
    def setUp(self):
        # self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser = webdriver.Chrome() 
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()
        
    def test_valid_login(self):
        pass
    
    def test_invalid_login(self):
        pass
    
    def test_password_visibility_toggle(self):
        pass
    
    def test_session_persistence(self):
        pass
    
    def test_logout_functionality(self):
        pass
