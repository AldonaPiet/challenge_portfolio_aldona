from pages.base_page import BasePage


class LoginPage(BasePage):
#Subtask 3: Dodawanie selektorów do projektu: uzupełnienie tej strony o elementy
# - i selektory dla nich - które nie zostały jeszcze umieszczone.

    login_field_xpath = "//*[@id="login"]"
    password_field_xpath = "//*[@id="password"]"
    sign_in_button_xpath = "//span[@class="MuiButton-label"]"
    remind_password_hyperlink_xpath = "//*[text()="Remind password" or text()="Przypomnij hasło"]"
    language_list_xpath = "//*[contains(@class,"selectMenu ")]"

   # Dodatkowo
   #  dostęp do nich tylko w trakcie wyboru języka:
   #  language_polish_xpath = "//*[@data-value = "pl"]"
   #  language_english_xpath = "//*[@data-value = "en"]"



    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
