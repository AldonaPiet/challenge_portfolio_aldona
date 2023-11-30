import os
import unittest
import time

from selenium import webdriver

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestDashboardPageLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login: LoginPage = LoginPage(self.driver)
        user_login.type_in_email('user06@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in()
        time.sleep(3)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_language_button()
        time.sleep(3)
        dashboard_page.click_language_button()
        #time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
