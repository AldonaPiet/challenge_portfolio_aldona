from pages.base_page import BasePage
#zad 3 sub 4

class AddPlayer(BasePage):
    expected_title = 'Add player'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title
