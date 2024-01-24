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
        # url = 'https://dareit.futbolkolektyw.pl/en'    # UAT

        url = "https://scouts-test.futbolkolektyw.pl/en"  # test

        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(
            executable_path=DRIVER_PATH)  # resolving error which showed up during 5th task without changing code -.-
        self.driver = webdriver.Chrome(
            service=self.driver_service)  # resolving error which showed up during 5th task without changing code -.-

        self.driver.get(url)
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        email_user = 'user06@getnada.com'
        password_user = 'Test-1234'
        dashboard_screenshots = "C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestDashboardPageLanguage/Polish.png"
        dashboard_screenshots_language = "C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestDashboardPageLanguage/English.png"

        user_login: LoginPage = LoginPage(self.driver)
        user_login.type_in_email(email_user)
        user_login.type_in_password(password_user)
        user_login.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_element_to_be_visible(Dashboard.last_updated_player_button_xpath)
        dashboard_page.click_language_button()
        dashboard_page.wait_for_element_to_be_visible(Dashboard.sign_out_button_xpath)
        self.driver.save_screenshot(dashboard_screenshots)
        dashboard_page.click_language_button()
        dashboard_page.wait_for_element_to_be_visible(Dashboard.language_button_xpath)
        self.driver.save_screenshot(dashboard_screenshots_language)

        dashboard_page.wait_for_element_to_be_clickable(dashboard_page.last_updated_player_button_xpath)
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
