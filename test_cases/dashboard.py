import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestDashboardPageLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)   # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        self.driver = webdriver.Chrome(service=self.driver_service)  # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        # self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login: LoginPage = LoginPage(self.driver)
        user_login.type_in_email('user06@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_element_to_be_visible(Dashboard.last_updated_player_button_xpath)
        dashboard_page.click_language_button()
        dashboard_page.wait_for_element_to_be_visible(Dashboard.sign_out_button_polish_xpath )
        self.driver.save_screenshot("C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestDashboardPageLanguage/Polish.png")
        dashboard_page.click_language_button()
        dashboard_page.wait_for_element_to_be_visible(Dashboard.language_button_polish_xpath )
        self.driver.save_screenshot("C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestDashboardPageLanguage/English.png")
        # do tego momentu test pozytywny, poniżej - sprawdzam czy przechodzi do następnej strony - test negatywny
        dashboard_page.wait_for_element_to_be_clickable(dashboard_page.last_updated_player_button_xpath)
        dashboard_page.title_of_page()


    @classmethod
    def tearDown(self):
        self.driver.quit()
