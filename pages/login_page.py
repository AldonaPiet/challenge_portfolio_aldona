from pages.base_page import BasePage


class LoginPage(BasePage):
    # url = 'https://dareit.futbolkolektyw.pl/en' # uat
    url = 'https://scouts-test.futbolkolektyw.pl/en'  # test
    email_user = 'user06@getnada.com'
    password_user = 'Test-1234'
    wrong_password = 'hgsgst-1234'
    expected_title = "Scouts panel - sign in"
    expected_header_of_box = 'Scouts Panel'
    # login_url = ('https://scouts-test.futbolkolektyw.pl/en') redundant - it could be used in get_page_title
    # but it's better to use more universal way where driver gets url from the website it currently tests.
    # I'm leaving that as memento ;)

    # XPaths
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[@class='MuiButton-label']"
    remind_password_hyperlink_xpath = "//*/a"
    language_list_xpath = "/*[contains(@class,'selectMenu')]"
    title_of_box_xpath = "//*/div[1]/h5"
    invalid_password_or_id_xpath = "//*/div[3]/span"

    # Additionally accessible only during choosing language:
    language_polish_xpath = "//*[@data-value = 'pl']"
    language_english_xpath = "//*[@data-value = 'en']"

    def type_in_email(self, email_user):
        self.field_send_keys(self.login_field_xpath, email_user)

    def type_in_password(self, password_user):
        self.field_send_keys(self.password_field_xpath, password_user)

    def click_sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_title_of_page(self):
        assert self.get_page_title() == self.expected_title

    def assert_header_text(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.expected_header_of_box)
