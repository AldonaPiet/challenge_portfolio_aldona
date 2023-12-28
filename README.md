
# Zadanie 1: Konfiguracja oprogramowania

Cel zadania:

* wykonać testy eksploracyjne aplikacji,

* dowiedzieć się jakie programy są niezbędne, aby rozpocząć testowanie automatyczne,

* założyć własne zdalne repozytorium w GitHubie,

* sklonować repozytorium i skonfigurować środowisko pracy,

* sformatować plik README. 


## Podzadanie 1:
## Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge


Zdecydowałam się wziąć udział w projekcie ponieważ chcę zostać testerką oprogramowania. 

Kiedy zdecydowałam się na testowanie naturalną, moim zdaniem, kolejnością było rozpocząć od  testowania manualnego i zaaplikowałam do programu mentoringowego Dare IT właśnie w tym zakresie. 

Nie mogłam mieć jednak pewności, że dostanę się do programu a "wyzwania" kończyły rejestrację jeszcze przed ogłoszeniem wyników naboru. 

Ponieważ bardzo mi zależy zapisałam się zatem do automatyzacji testów - może to nie po kolei ale nie mam wyjścia, potrzebuję zdobyć praktyczne umiejętności i poznać dobre praktyki a tylko doświadczeni testerzy mogą mi je przekazać :)

Planowałam, w razie przyjęcia mnie do programu mentoringowego, że pociągnę oba jednocześnie. Nie byłoby łatwo ale kto da radę jak nie ja :D 
Nie mam jednak przed sobą tego szalonego wyzwania, ponieważ nie zostałam przyjęta. Przyszłość pokaże czy dobrze się stało ;)  

Szczęśliwie zdaje się, że robienie rzeczy w odwrotnej kolejności ostatnio mi wychodzi - zdałam ostatnio egzamin ISTQB,
choć praktyki nie mam żadnej i kiedy zaczynałam się uczyć poczułam, że sylabus mógł być równie dobrze napisany w domowolnym 
języku, w którym rozumiem podstawowe zwroty...kosmos jakiś.

Po przeczytaniu najdłuższych 70 stron w moim życiu wykupiłam sobie bootcamp na Udemy - wiedziałam, że nie da mi zbyt praktycznych umiejętności ale pomoże zrozumieć język, w którym sylabus jest napisany ;) 

I zadziałało pięknie :) Następne podejście do sylabusa już było nauką a nie rozszyfrowywaniem znaczenia słów.

Ale zdany egzamin to tylko certyfikat. W moim przypadku udowadnia, 
że pojmuję teorię i potrafię przyswajać wiedzę. 
Do praktyki daleko i tym samym do zdobycia odpowiednich kwalifikacji i do zatrudnienia.

Podsumowując:
- Mój cel: zostać testerem.
- Motywacja: wewnętrzna.
- Oczekiwania względem projektu: zdobycie praktycznych umiejętności, na które mogą się połakomić, (i nie zawieść),  pracodawcy.

## Podzadanie 4:

### Wynik: 12/14

Pytania, w których zrobiłam błąd i poprawna odpowiedź:

"Inspekcje pozwalają wykryć wszystkie z poniższych za wyjątkiem:"

ODP: "Jak wiele kodu zostało pokryte testami"

"Które z poniższych jest jednym z GŁÓWNYCH zadań implementacji i wykonania testów?"

ODP: "Raportowanie rozbieżności jako incydentów"



***

# Zadanie 2: Selektory

Cel zadania:

* dowiedzieć się czym są selektory,
* dowiedzieć się gdzie szukać selektorów,
* poznać zapis xPath’ów, 
* zrozumieć czym się kierować, aby wyodrębnić te “najlepsze” selektory.


## Podzadanie 2:

1. Wypisać wszystkie elementy znajdujące się na [stronie logowania](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true);
2. Pod każdym elementem wymienić 3 działające selektory (nie muszą być unikalne, ważne jest tylko to, aby działały.

### Moje założenia:
Szukam elementów na stronie, które są "aktywne" tzn. można je uzupełnić lub mogą nas gdzieś przenieść
  (czyli np tło itp. się nie liczy).

### Rozwiązanie:

login_input_xpath =

* //*[@id='login']
* //input[@name='login']
* //*[contains(@class,'MuiIn' )]//descendant::input[@id='login']

password_input_xpath =

* //*[@id='password']
* //*[@name='password']
* //input[@type='password']

remind_input_hyperlink_xpath =

* //*[@id="__next"]/form/div/div[1]/a
* //*[text()='Remind password' or text()='Przypomnij hasło']
* //descendant::div/a

language_list_xpath =
* //*[@id='__next']/form/div/div[2]/div/div
* //*[contains(@class,'selectMenu')]
* //*[@id='__next']/form/div/div[2]/div/input//preceding-sibling::div

sign_in_button_xpath =

* //*[@id='__next']/form/div/div[2]/button/span[1]
* //*[@class='MuiButton-label']
* //span[contains(@class,'MuiBut')]

#### Dodatkowo
_UWAGA: Ten fragment kodu 
pojawia się w DevToolsach tylko kiedy zostanie 
wybrane/kliknięte okno wyboru języka._


language_polish_xpath =

* //*[@id="menu-"]/div[3]/ul/li[1]
* //*[@data-value="pl"]
* //ul[@role="listbox"]//child::li[@tabindex="-1"]

language_english_xpath =
* //*[@id="menu-"]/div[3]/ul/li[2]
* //*[@data-value="en"]
* //ul[@role="listbox"]//child::li[@tabindex="0"]

# Zadanie 3: Pierwszy test automatyczny i asserty

Cel zadania:

* poznać framework, na którym będziemy pracować,
* klikać w elementy na stronie,
* wypełniać pola tekstem,
* wykorzystać assert title, 
* uruchomić test.

# Zadanie 4: Refactor, debugger i przypadki testowe

Cel zadania:

* wykonać refactor naszego kodu,  
* dowiedzieć się jak pracować z debuggerem,  
* rozwinąć skrzydła wyobraźni- zaprojektujesz i napiszesz test case’y,  
* zautomatyzować stronę internetową na podstawie swoich TC.


# Zadanie 5: Robot Framework

Cel zadania:

* dowiedzieć się czym jest Smoke Tests  
* dowiedzieć się jak skonfigurować Suite Test  
* poznać nowy framework,  
* wygenerować automatycznie raport



# Zadanie 6: Zgłaszanie błędów i raport z testów

Cel zadania:

* Wykorzystać projekty w jedynym słusznym celu - wyłapywaniu bugów,  
* Zapoznać się ze strukturą prawidłowo zgłoszonego buga,  
* Zapoznać się ze strukturą raportów z testów,
* Stworzyć repozytorium z funkcjonalnym portfolio w README file. <a href="https://github.com/AldonaPiet/Portfolio">PORTFOLIO</a>
