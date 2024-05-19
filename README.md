# Dare IT Challenge - Testy Automatyczne + Python 
## Zadanie 1: Konfiguracja oprogramowania

Cel zadania:

* wykonać testy eksploracyjne aplikacji,
* dowiedzieć się jakie programy są niezbędne, aby rozpocząć testowanie automatyczne,
* założyć własne zdalne repozytorium w GitHubie,
* sklonować repozytorium i skonfigurować środowisko pracy,
* sformatować plik README. 


### Podzadanie 1:
#### Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge

Chcę zostać testerką oprogramowania. 

Kiedy zdecydowałam się na testowanie zaaplikowałam do programu mentoringowego Dare IT w zakresie testowania manualnego. 

Nie mogłam mieć jednak pewności, że dostanę się do programu i jendocześnie zapisałam się do Dare IT Challenge - potrzebuję zdobyć praktyczne umiejętności i poznać dobre praktyki zatem, na okoliczność nie przyjęcia mnie do programu mentoringowego, nadal miałabym szansę na rozwijanie umiejętności pod okiem doświadczonych testerów. I tak właśnie się stało 🙂

Zdałam ostatnio egzamin ISTQB FL, ale zdany egzamin to tylko certyfikat. W moim przypadku udowadnia, 
że pojmuję teorię i potrafię przyswajać wiedzę. 
Do praktyki daleko i tym samym do zdobycia odpowiednich kwalifikacji i do zatrudnienia - dlatego zdecydowałam się wziąć udział w wyzwaniu <a href="https://www.dareit.io/challenges/wstep-do-testow-automatycznych" >Dare IT Challenge</a>

Podsumowując:
- Mój cel: zostać testerem.
- Motywacja: wewnętrzna.
- Oczekiwania względem projektu: zdobycie praktycznych umiejętności, na które mogą się połakomić (i nie zawieść) pracodawcy.

### Podzadanie 4:
#### Zrobić <a href = "https://getistqb.com/#quizzes">test</a> purpurowy
#### Wynik: 12/14

Pytania, w których zrobiłam błąd i poprawna odpowiedź:

"Inspekcje pozwalają wykryć wszystkie z poniższych za wyjątkiem:"

ODP: "Jak wiele kodu zostało pokryte testami"

"Które z poniższych jest jednym z GŁÓWNYCH zadań implementacji i wykonania testów?"

ODP: "Raportowanie rozbieżności jako incydentów"



***

## Zadanie 2: Selektory

Cel zadania:

* dowiedzieć się czym są selektory,
* dowiedzieć się gdzie szukać selektorów,
* poznać zapis xPath’ów, 
* zrozumieć czym się kierować, aby wyodrębnić te “najlepsze” selektory.


### Podzadanie 2:

1. Wypisać wszystkie elementy znajdujące się na [stronie logowania](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true);
2. Pod każdym elementem wymienić 3 działające selektory (nie muszą być unikalne, ważne jest tylko to, aby działały.

#### Moje założenia:
Szukam elementów na stronie, które są "aktywne" tzn. można je uzupełnić lub mogą nas gdzieś przenieść
  (czyli np tło itp. się nie liczy).

#### Rozwiązanie:

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

##### Dodatkowo
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

## Zadanie 3: Pierwszy test automatyczny i asserty

Cel zadania:

* poznać framework, na którym będziemy pracować,
* klikać w elementy na stronie,
* wypełniać pola tekstem,
* wykorzystać assert title, 
* uruchomić test.

## Zadanie 4: Refactor, debugger i przypadki testowe

Cel zadania:

* wykonać refactor naszego kodu,  
* dowiedzieć się jak pracować z debuggerem,  
* rozwinąć skrzydła wyobraźni- zaprojektujesz i napiszesz test case’y,  
* zautomatyzować stronę internetową na podstawie swoich TC.


## Zadanie 5: Robot Framework

Cel zadania:

* dowiedzieć się czym jest Smoke Tests  
* dowiedzieć się jak skonfigurować Suite Test  
* poznać nowy framework,
* testy wcześniej zrobione w pythonie przełożyć na RF
* wygenerować automatycznie raport



## Zadanie 6: Zgłaszanie błędów i raport z testów

Cel zadania:

* Wykorzystać projekty w jedynym słusznym celu - wyłapywaniu bugów,  
* Zapoznać się ze strukturą prawidłowo zgłoszonego buga,  
* Zapoznać się ze strukturą raportów z testów,
* Stworzyć repozytorium z funkcjonalnym portfolio w README file. <a href="https://github.com/AldonaPiet/Portfolio">🔗PORTFOLIO</a>



