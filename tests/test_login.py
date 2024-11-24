import time

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage



# Positive test case
def test_login_success(android_driver):
    login_page = LoginPage(android_driver)
    login_page.select_germany()
    login_page.select_english()
    login_page.agree()
    login_page.go_to_login()
    login_page.login('test@automation.com', 'Qwerty1Z!')
    login_page.skip()
    assert login_page.is_hello_message_displayed(), "Hello message is not displayed"
    assert login_page.is_navigation_bar_shown(), "Navigation bar is not displayed"


# Negative test cases
def test_login_invalid_credentials(android_driver):
    login_page = LoginPage(android_driver)
    login_page.select_germany()
    login_page.select_english()
    login_page.agree()
    login_page.go_to_login()
    login_page.login('incorrect@email.com', 'incorrect!')
    assert login_page.is_incorrect_email_message_displayed(), "Incorrect email message is not displayed"
    assert login_page.is_incorrect_password_message_displayed(), "Incorrect password message is not displayed"
    assert login_page.is_hello_message_displayed(), "Hello message is not displayed"
    assert login_page.is_navigation_bar_shown(), "Navigation bar is not displayed"

