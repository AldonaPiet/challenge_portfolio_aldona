import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


# zad 3 sub 4
class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)   # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        self.driver = webdriver.Chrome(service=self.driver_service)  # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        # self.driver.get('https://dareit.futbolkolektyw.pl/en')
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

class TestAddPlayerForm(unittest.TestCase):

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

    def test_add_player_form(self):
        #url = 'https://scouts-test.futbolkolektyw.pl/en'
        email_user = 'user06@getnada.com'
        password = 'Test-1234'
        email_player = 'APkhuhyugb@gmail.com'
        name = 'APolinariana'
        surname = 'APairanilofilo'
        phone = '12345623456'
        weight_value = '70'
        height_value = '170'
        birth_date = '03.09.2003'
        club = 'APtfxfghjk'
        previous_club = 'OPlalkknsjbdh'
        level = 'APokjgjgfg5hkkj'
        main_position = 'APany'
        second_position = 'APstillany'
        achievements = 'none'
        language_player = 'French'
        laczy_nas_pilka = 'APaleocochodzi'
        minut_90 = 'APaleocochodzistill'
        # FB = 'none'
        YouTube = 'https://www.youtube.com/watch?v=Emanhr-eLWg'



        user_login = LoginPage(self.driver)
        user_login.type_in_email(email_user)
        user_login.type_in_password(password)
        user_login.wait_for_element_to_be_clickable(LoginPage.sign_in_button_xpath)

        user_login.click_sign_in()
        user_dashboard = Dashboard(self.driver)
        user_dashboard.wait_for_element_to_be_clickable(Dashboard.Add_player_button_xpath)

        user_dashboard.click_add_player()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.wait_for_element_to_be_clickable(AddPlayer.email_field_player_xpath)

        # filling in the form:
        add_a_player_page.click_district_option_button()
        add_a_player_page.wait_for_element_to_be_clickable(AddPlayer.district_choice_lower_silesia_xpath)
        add_a_player_page.click_district_choice()
        add_a_player_page.type_in_height_value(height_value)
        add_a_player_page.type_in_email_player(email_player)
        add_a_player_page.type_in_name(name)
        add_a_player_page.type_in_surname(surname)
        add_a_player_page.type_in_birth_date(birth_date)
        add_a_player_page.type_in_main_position(main_position)
        add_a_player_page.type_in_phone(phone)
        add_a_player_page.type_in_weight_value(weight_value)
        add_a_player_page.click_leg_option_button()
        add_a_player_page.click_leg_choice_right_button()
        add_a_player_page.type_in_club(club)
        add_a_player_page.type_in_previous_club(previous_club)
        add_a_player_page.type_in_level(level)
        add_a_player_page.type_in_second_position(second_position)
        add_a_player_page.type_in_achievements(achievements)
        add_a_player_page.click_language_player()
        add_a_player_page.type_in_language_player(language_player)
        add_a_player_page.type_in_laczy_nas_pilka(laczy_nas_pilka)
        add_a_player_page.type_in_minut_90(minut_90)
        # add_a_player_page.type_in_FB(FB)
        add_a_player_page.click_YouTube()
        add_a_player_page.type_in_YouTube(YouTube)
        add_a_player_page.wait_for_element_to_be_clickable(AddPlayer.submit_button_xpath)
        add_a_player_page.click_submit_button()
        add_a_player_page.wait_for_element_to_be_clickable(AddPlayer.Main_page_xpath)
        add_a_player_page.click_main_page_button()
        user_dashboard = Dashboard(self.driver)
        user_dashboard.wait_for_element_to_be_clickable(Dashboard.last_created_player_button_xpath)
        self.driver.save_screenshot("C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestAddPlayerForm/see_last_created_player.png")
        user_dashboard.click_last_created_player()




    @classmethod
    def tearDown(self):
        self.driver.quit()

class TestUpdateLastCreatedPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)   # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        self.driver = webdriver.Chrome(service=self.driver_service)  # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        # self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_update_last_created_player_form(self):
        email_user = 'user06@getnada.com'
        password = 'Test-1234'
        language_player_1 = 'Portuguese'
        previous_club = 'hokuiadsag'

        user_login: LoginPage = LoginPage(self.driver)
        user_login.type_in_email(email_user)
        user_login.type_in_password(password)
        user_login.wait_for_element_to_be_clickable(LoginPage.sign_in_button_xpath)
        user_login.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_element_to_be_clickable(Dashboard.Add_player_button_xpath)
        dashboard_page.click_last_created_player()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.click_language_player()
        add_a_player_page.type_in_language_player_1(language_player_1)
        add_a_player_page.type_in_previous_club(previous_club)
        add_a_player_page.wait_for_element_to_be_clickable(add_a_player_page.submit_button_xpath)
        add_a_player_page.click_submit_button()
        self.driver.save_screenshot("C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestUpdateLastCreatedPlayerForm/see_last_updated_player.png")


    @classmethod
    def tearDown(self):
        self.driver.quit()


class TestUpdateWrongLastCreatedPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)   # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        self.driver = webdriver.Chrome(service=self.driver_service)  # rozwiązania problemu który wyskoczył przy zadaniu 5 bez jakiejkolwiek zmiany kodu
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        # self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_update_wrong_last_created_player_form(self):
        email_user = 'user06@getnada.com'
        password = 'Test-1234'

        wrong_email_player = 'APpppppgmailcom'
        wrong_birth_date = '10000000000'
        wrong_phone = '#$%^&*()(*&^%$%^&*'
        wrong_height_value = 'aaaaaaaa'
        previous_club = 'hokuiadsag'


        # date2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="date-picker_to"]')))
        # date2.click()
        # date2.send_keys(Keys.CONTROL + "a")
        # date2.send_keys(Keys.DELETE)
        # date2.send_keys("15/11/2021")

        # date2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="date-picker_to"]')))
        # date2.click()
        # date2.clear()
        # date2.send_keys("15/11/2021")

        user_login: LoginPage = LoginPage(self.driver)
        user_login.type_in_email(email_user)
        user_login.type_in_password(password)
        user_login.wait_for_element_to_be_clickable(LoginPage.sign_in_button_xpath)
        user_login.click_sign_in()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_element_to_be_clickable(Dashboard.Add_player_button_xpath)
        dashboard_page.click_last_created_player()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.type_in_birth_date(wrong_birth_date)
        self.driver.save_screenshot("C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestUpdateWrongLastCreatedPlayerForm/updated_wrong_birth.png")
        add_a_player_page.type_in_phone(wrong_phone)
        self.driver.save_screenshot(
            "C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestUpdateWrongLastCreatedPlayerForm/updated_wrong_phone.png")
        add_a_player_page.type_in_height_value(wrong_height_value)
        self.driver.save_screenshot(
            "C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestUpdateWrongLastCreatedPlayerForm/updated_wrong_height.png")
        # add_a_player_page.type_in_email_player(wrong_email_player)
        # self.driver.save_screenshot(
        #     "C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestUpdateWrongLastCreatedPlayerForm/updated_wrong_e-mail.png")
        add_a_player_page.type_in_previous_club(previous_club)
        add_a_player_page.click_submit_button()
        self.driver.save_screenshot(
            "C:/Users/Aldona/Documents/GitHub/challenges/challenge_portfolio_aldona/screenshots/Scrsht_TestUpdateWrongLastCreatedPlayerForm/updated_wrong_data.png")


    @classmethod
    def tearDown(self):
        self.driver.quit()