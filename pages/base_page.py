from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH): #wpisanie tekstu w pole tekstowe
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH): #kliknięcie w wybrany element
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url): #zad 3 sub 3
        # self.driver.get(url) #kiedy tego nie ma działa tak samo w opisie tego fragmentu nie ma a na zdjęcach i filmiku jest
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text): #zad 3 sub 5*
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text, 'Upewnij się co do tekstu który porównujesz'
