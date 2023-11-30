from pages.base_page import BasePage
import time


# zad. 2 Subtask 4: Dodanie nowego pliku
# Utwórz nowy plik w folderze pages i dodaj klasę oraz selektory do elementów na kolejnej stronie.
# min 10 selektorów z dashboardu a najlepiej wszystkie

# moje założenia:
# szukam elementów, w które można kliknąć
# linki działają w obu wersjach językowych
# tam gdzie to, moim zdaniem, możliwe skracam linka

class Dashboard(BasePage):  # zad 3  - poniżej xPathów

    Main_page_xpath = "//*[text() ='Strona główna' or text()='Main page']"
    Players_button_xpath = "//*[text() ='Gracze' or text()='Players']"

    language_button_xpath = "//*[text() ='English' or text()='Polski']"
    sign_out_button_xpath = "//*[text() ='Wyloguj' or text()='Sign out']"
    dev_team_contact_button_xpath = "//*[text() ='Dev team contact']"  # nota bene mamy tutaj opis po angielsku w obu wersjach językowych
    #Add_player_button_xpath = "//*[text() ='Dodaj gracza' or text()='Add player']"
    Add_player_button_xpath = "//*/div[2]/div/div/a/button"
    # poniżej mam problem z jednoznacznym określeniem elementu, dlatego wykorzystuję copy xpath
    # choć wiem, że jest to podatne na zmiany
    # nie chcę wykorzystać text() i contains bo tekst zmieni się tutaj
    # prawdopodobnie szybciej niż struktura dokumentu html

    last_created_player_button_xpath = "//*/div[3]/div/div/a[1]/button"
    last_updated_player_button_xpath = "//*/a[2]/button"
    last_created_match_button_xpath = "//*/a[3]/button"
    last_updated_match_button_xpath = "//*/a[4]/button"
    last_updated_report_button_xpath = "//*/a[5]/button"
    # zad 3 sub 3
    expected_title = "Scouts panel"
    #dashboard_url = 'https://scouts-test.futbolkolektyw.pl/' zbędny - mógł być użyty do get_page_title ale lepiej korzystać z bardziej uniwersalnej opcji gdzie driver pobiera url strony na której testuje

    def title_of_page(self):  # zad 3 sub 3
        self.wait_for_element_to_be_clickable(self.Last_created_match_button_xpath)
        assert self.get_page_title() == self.expected_title

    def click_add_player(self):  # zad 3 sub 4
        self.click_on_the_element(self.Add_player_button_xpath)

    def click_language_button(self):  # zad 3 sub 4
        self.click_on_the_element(self.language_button_xpath)

    def click_sign_out(self):  # zad 3 sub 4
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_last_created_player(self):  # zad 3 sub 4
        self.click_on_the_element(self.last_created_player_button_xpath)

# pass
