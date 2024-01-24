import os
import unittest
# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class TestLoginPage(unittest.TestCase):
    # data used in the code below:
    # url = 'https://dareit.futbolkolektyw.pl/en'    # UAT
    # url = "https://scouts-test.futbolkolektyw.pl/en"   # test
    # email_user = 'user06@getnada.com'
    # password_user = 'Test-1234'
    # wrong_password = 'hgsgst-1234'

    @classmethod
    def setUp(self):
        url = "https://scouts-test.futbolkolektyw.pl/en" # test
        # url = 'https://dareit.futbolkolektyw.pl/en' # UAT

        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)   # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu (bo w 5 zad. robiliśmy inny framework)
        self.driver = webdriver.Chrome(service=self.driver_service)  # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu (bo w 5 zad. robiliśmy inny framework)
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH) # w komentarzu <=> próby naprawy błedu

        self.driver.get(url)
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        email_user = 'user06@getnada.com'
        password_user = 'Test-1234'

        user_login: LoginPage = LoginPage(self.driver)
        # user_login.check_title_of_page() # assertion off on UAT
        # user_login.assert_header_text()   # assertion off on UAT (left only at the end)
        user_login.type_in_email(email_user)
        user_login.type_in_password(password_user)
        user_login.wait_for_element_to_be_clickable(LoginPage.sign_in_button_xpath)
        user_login.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_element_to_be_clickable(dashboard_page.last_updated_player_button_xpath)
        dashboard_page.title_of_page()



    @classmethod
    def tearDown(self):
        self.driver.quit()

class TestLoginPageWrongData(unittest.TestCase):


    @classmethod
    def setUp(self):
        # url = 'https://dareit.futbolkolektyw.pl/en' # UAT
        url = 'https://scouts-test.futbolkolektyw.pl/en'  # test
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)   # resolving error which showed up during 5th task without changing code -.-
        self.driver = webdriver.Chrome(service=self.driver_service)  # resolving error which showed up during 5th task without changing code -.-
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        self.driver.get(url)
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system_wrong_data(self):

        email_user = 'user06@getnada.com'
        # password_user = 'Test-1234'  # in case one wanted to check does it work with valid password
        wrong_password = 'hgsgst-1234'
        screenshots_folder = 'C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestLoginPageWrongData/LPWrongData.png'

        user_login: LoginPage = LoginPage(self.driver)
        user_login.type_in_email(email_user)
        user_login.type_in_password(wrong_password)
        user_login.wait_for_element_to_be_clickable(LoginPage.sign_in_button_xpath)

        user_login.click_sign_in()
        user_login.wait_for_element_to_be_visible(LoginPage.invalid_password_or_id_xpath)

        self.driver.save_screenshot(screenshots_folder)
        # until now positive test - as of below negative test - we are checking does it go to the next page
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_element_to_be_clickable(dashboard_page.last_updated_player_button_xpath)
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()