from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[@class='MuiButton-label']"
    remind_password_hyperlink_xpath = "//*[text()='Remind password' or text()='Przypomnij hasło']"
    language_list_xpath = "/*[contains(@class,'selectMenu')]"
    title_of_box_xpath = "//*/div[1]/h5"
    invalid_password_or_id_xpath = "//*/div[3]/span"
    # login_url = ('https://scouts-test.futbolkolektyw.pl/en') zbędny - mógł być użyty do get_page_title ale lepiej
    # korzystać z bardziej uniwersalnej opcji gdzie driver pobiera url strony na której testuje
    expected_title = "Scouts panel - sign in"
    expected_header_of_box = 'Scouts Panel'

    # Dodatkowo
    #  dostęp do nich tylko w trakcie wyboru języka:
    language_polish_xpath = "//*[@data-value = 'pl']"
    language_english_xpath = "//*[@data-value = 'en']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_title_of_page(self):
        assert self.get_page_title() == self.expected_title  # sam pobiera url ze strony na której testuje

    def assert_header_text(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.expected_header_of_box)



