import os
import unittest
import time

from selenium import webdriver

from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

#zad 3 sub 4
class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user06@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in()
        user_dashboard = Dashboard(self.driver)
        user_dashboard.click_add_player()
        time.sleep(5)
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()