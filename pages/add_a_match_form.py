from pages.base_page import BasePage


class AddMatchForm(BasePage):

# Subtask 5: create new file in pages folder,
# add class and selectors - at least 10 on the page add a match form.

main_page_xpath = "//*/ul[1]/div[1]/div[2]/span"
players_button_xpath = "//*/ul[1]/div[2]/div[2]/span"

edit_certain_player_button_xpath = "//ul[2]/div[1]/div[2]/span"
player_matches_button_xpath = "//*/ul[2]/div[2]/div[2]/span"
player_reports_button_xpath = "//*/div[3]/div[2]/span"

language_button_xpath = "//*/ul[3]/div[1]/span"
sign_out_button_xpath = "//*/ul[3]/div[2]/div[2]/span"

my_team_input_xpath = "//*[@name='myTeam']"
enemy_team_input_xpath = "//*[@name='enemyTeam']"
my_team_score_input_xpath = "//*[@name='myTeamScore']"
enemy_team_score_input_xpath = "//*[@name='enemyTeamScore']"

date_input_xpath = "//*[@name='date']"
match_at_home_button_xpath = "//*/label[1]/span[2]"
match_at_home_radio_button_xpath = "//*/label[1]/span[1]/span[1]/input"
match_out_home_button_xpath = "//*/label[2]/span[2]"
match_out_home_radio_button_xpath = "//*/label[2]/span[1]/span[1]/input"

tshirt_color_input_xpath = "//*[@name='tshirt']"
league_input_xpath = "//*[@name='league']"
time_played_input_xpath = "//*[@name='timePlayed']"
number_input_xpath = "//*[@name='number']"
web_match_input_xpath = "//*[@name='webMatch']"
general_input_xpath = "//*[@name='general']"
rating_input_xpath = "//*[@name='rating']"

submit_input_xpath = "//*[text()='Submit']"
clear_input_xpath = "//*[text()='Clear']"

pass
