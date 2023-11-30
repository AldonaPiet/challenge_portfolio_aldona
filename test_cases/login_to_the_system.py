import os
import unittest
import time

from selenium import webdriver

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


# zad 3 sub 2
class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login: LoginPage = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.assert_header_text()  # zad 3 sub 5*
        user_login.type_in_email('user06@getnada.com')
        user_login.type_in_password('Test-1234')
        # user_login.wait_for_element_to_be_clickable(LoginPage.sign_in_button_xpath)
        user_login.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        # time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

class TestLoginPageWrongData(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        email_user = 'user06@getnada.com'
        password = 'Test-1234'
        wrong_password = 'hgsgst-1234'

        user_login: LoginPage = LoginPage(self.driver)
        user_login.type_in_email(email_user)
        user_login.type_in_password(password)
        user_login.click_sign_in()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_sign_out()
        time.sleep(2)
        user_login.type_in_email(email_user)
        user_login.type_in_password(wrong_password)
        user_login.click_sign_in()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()