from pages.base_page import BasePage


# zad 3 sub 4

class AddPlayer(BasePage):
    # data:
    email_user = 'user06@getnada.com'
    password_user = 'Test-1234'
    expected_title = 'Add player'

    # XPaths:
    main_page_xpath = "//*/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*/ul[1]/div[2]/div[2]/span"

    language_button_xpath = "//*/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*/ul[2]/div[2]/div[2]/span"

    edit_certain_player_button_xpath = "//ul[2]/div[1]/div[2]/span"

    # form:
    email_field_player_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"  # mandatory
    surname_field_xpath = "//*[@name='surname']"  # mandatory
    phone_field_xpath = "//*[@name='phone']"
    weight_value_field_xpath = "//*[@name='weight']"
    height_value_field_xpath = "//*[@name='height']"
    birth_date_field_xpath = "//*[@name='age']"  # mandatory = Age
    leg_option_button_xpath = "//*[@id='mui-component-select-leg']"
    leg_choice_right_xpath = "//*[@data-value='right']"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name='level']"
    main_position_field_xpath = "//*[@name='mainPosition']"  # mandatory
    second_position_field_xpath = "//*[@name='secondPosition']"
    district_option_button_xpath = "//*[@id='mui-component-select-district']"
    district_choice_lower_silesia_xpath = "//*[@data-value='dolnoslaskie']"
    achievements_field_xpath = "//*[@name='achievements']"
    language_player_button_xpath = "//*/div[15]/button/span[1]"
    language_player_field_xpath = "//*[@name='languages[0]']"
    language_player_field_1_xpath = "//*[@name='languages[1]']"
    laczy_nas_pilka_field_xpath = "//*[@name='webLaczy']"
    minut_90_field_xpath = "//*[@name='web90']"
    fb_field_xpath = "//*[@name='webFB']"
    youtube_button_xpath = "//*/div[19]/button/span[1]"
    youtube_field_xpath = "//*[@name='webYT[0]']"
    previous_club_xpath = "//*[@name='prevClub']"
    submit_button_xpath = "//*[@type='submit']"

    def type_in_email_player(self, email_player):
        self.field_send_keys(self.email_field_player_xpath, email_player)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_birth_date(self, birth_date):
        self.field_send_keys(self.birth_date_field_xpath, birth_date)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight_value(self, weight_value):
        self.field_send_keys(self.weight_value_field_xpath, weight_value)

    def type_in_height_value(self, height_value):
        self.field_send_keys(self.height_value_field_xpath, height_value)

    def click_leg_option_button(self):
        self.click_on_the_element(self.leg_option_button_xpath)

    def click_leg_choice_right_button(self):
        self.click_on_the_element(self.leg_choice_right_xpath)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_previous_club(self, previous_club):
        self.field_send_keys(self.previous_club_xpath, previous_club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def click_district_option_button(self):
        self.click_on_the_element(self.district_option_button_xpath)

    def click_district_choice(self):
        self.click_on_the_element(self.district_choice_lower_silesia_xpath)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def click_language_player(self):
        self.click_on_the_element(self.language_player_button_xpath)

    def type_in_language_player(self, language_player):
        self.field_send_keys(self.language_player_field_xpath, language_player)

    def type_in_language_player_1(self, language_player_1):
        self.field_send_keys(self.language_player_field_1_xpath, language_player_1)

    def type_in_laczy_nas_pilka(self, laczy_nas_pilka):
        self.field_send_keys(self.laczy_nas_pilka_field_xpath, laczy_nas_pilka)

    def type_in_minut_90(self, minut_90):
        self.field_send_keys(self.minut_90_field_xpath, minut_90)

    def type_in_FB(self, fb):
        self.field_send_keys(self.fb_field_xpath, fb)

    def click_YouTube(self):
        self.click_on_the_element(self.youtube_button_xpath)

    def type_in_YouTube(self, youtube):
        self.field_send_keys(self.youtube_field_xpath, youtube)

    # def type_in_main_position(self, main_position):
    #     self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_main_page_button(self):
        self.click_on_the_element(self.main_page_xpath)

    def title_of_page(self):
        assert self.get_page_title() == self.expected_title
