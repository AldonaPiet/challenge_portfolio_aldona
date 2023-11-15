from pages.base_page import BasePage


class Dashboard(BasePage):
# Subtask 4: Dodanie nowego pliku
# Utwórz nowy plik w folderze pages i dodaj klasę oraz selektory do elementów na kolejnej stronie.
# min 10 selektorów z dashboardu a najlepiej wszystkie

# moje założenia:
# szukam elementów, w które można kliknąć
# linki działają w obu wersjach językowych
# tam gdzie to, moim zdaniem, możliwe skracam linka

Main_page_xpath = "//*[text() ='Strona główna' or text()='Main page']"
Players_button_xpath = "//*[text() ='Gracze' or text()='Players']"

Language_button_xpath = "//*[text() ='English' or text()='Polski']"
Sign_out_button_xpath = "//*[text() ='Wyloguj' or text()='Sign out']"

Dev_team_contact_button_xpath = "//*[text() ='Dev team contact']" #nota bene mamy tutaj opis po angielsku w obu wersjach językowych
Add_player_button_xpath = "//*[text() ='Dodaj gracza' or text()='Add player']"

#poniżej mam problem z jednoznacznym określeniem elementu, dlatego wykorzystuję copy xpath
# choć wiem, że jest to podatne na zmiany
# nie chcę wykorzystać text() i contains bo tekst zmieni się tutaj
# szybciej niż struktura dokumentu html

Last_created_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
Last_updated_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
Last_created_match_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
Last_updated_match_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1]"
Last_updated_report_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"

pass