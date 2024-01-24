from pages.base_page import BasePage
import time


# moje założenia:
# szukam elementów, w które można kliknąć
# linki działają w obu wersjach językowych
# tam gdzie to, moim zdaniem, możliwe skracam link

class Dashboard(BasePage):
    # XPaths:
    main_page_xpath = "//*/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*/ul[1]/div[2]/div[2]/span"
    language_button_xpath = "//*/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*/ul[2]/div[2]/div[2]/span"
    dev_team_contact_button_xpath = "//*/a/span[1]"
    add_player_button_xpath = "//*/div[2]/div/div/a/button"
    last_created_player_button_xpath = "//*/div[3]/div/div/a[1]/button"
    last_updated_player_button_xpath = "//*/a[2]/button"
    last_created_match_button_xpath = "//*/a[3]/button"
    last_updated_match_button_xpath = "//*/a[4]/button"
    last_updated_report_button_xpath = "//*/a[5]/button"

    # data:
    expected_title = "Scouts panel"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.last_created_match_button_xpath)
        assert self.get_page_title() == self.expected_title

    def click_add_player(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_language_button(self):
        self.click_on_the_element(self.language_button_xpath)

    def click_sign_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_last_created_player(self):
        self.click_on_the_element(self.last_created_player_button_xpath)
