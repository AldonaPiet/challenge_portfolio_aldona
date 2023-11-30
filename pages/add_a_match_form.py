from pages.base_page import BasePage


class AddMatchForm(BasePage):


# Subtask 5: Dodanie nowego pliku
# Utwórz nowy plik w folderze pages i dodaj klasę oraz selektory
# do elementów na kolejnej stronie.
# min 10 selektorów z ADD A MATCH FORM a najlepiej wszystkie


Main_page_xpath = "//*[text() ='Strona główna' or text()='Main page']"
Players_button_xpath = "//*[text() ='Gracze' or text()='Players']"

Edit_certain_player_button_xpath = "//ul[2]/div[1]/div[2]/span"
Player_matches_button_xpath = "//*[text() ='Mecze' or text()='Matches']"
Player_reports_button_xpath = "//*[text() ='Raporty' or text()='Reports']"

Language_button_xpath = "//*[text() ='English' or text()='Polski']"
Sign_out_button_xpath = "//*[text() ='Wyloguj' or text()='Sign out']"

My_team_input_xpath = "//*[@name='myTeam']"
Enemy_team_input_xpath = "//*[@name='enemyTeam']"
My_team_score_input_xpath = "//*[@name='myTeamScore']"
Enemy_team_score_input_xpath = "//*[@name='enemyTeamScore']"

Date_input_xpath = "//*[@name='date']"
Match_at_home_button_xpath = "//*[text()='Match at home' or text()='Mecz domowy']"
Match_at_home_radio_button_xpath = "//*[@role='radiogroup']//span[1]//span[1]//input[@value='true']"
Match_out_home_button_xpath = "//*[text()='Match out home' or text()='Mecz wyjazdowy']"
Match_out_home_radio_button_xpath = "//*[@role='radiogroup']//span[1]//span[1]//input[@value='false']"

T - shirt_color_input_xpath = "//*[@name='tshirt']"
League_input_xpath = "//*[@name='league']"
Time_played_input_xpath = "//*[@name='timePlayed']"
Number_input_xpath = "//*[@name='number']"
Web_match_input_xpath = "//*[@name='webMatch']"  # w obu wersjach językowych mamy opis pola po angielsku na stronie
General_input_xpath = "//*[@name='general']"  # w obu wersjach językowych mamy opis pola po angielsku na stronie
Rating_input_xpath = "//*[@name='rating']"

Submit_input_xpath = "//*[text()='Submit']"  # w obu wersjach językowych mamy opis przycisku po angielsku na stronie
Clear_input_xpath = "//*[text()='Clear']"  # w obu wersjach językowych mamy opis przycisku po angielsku na stronie

pass
