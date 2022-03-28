# Alkomat-Systemy_Wbudowane
Projekt zaliczeniowy z przedmiotu Systemy Wbudowane 

### Cel projektu:
Celem projektu jest zaprojektowanie układu, którego zadaniem będzie mierzenie alkoholu w wydychanym 
powietrzu pracowników firmy. Dodatkowo wyniki będą wyświetlane na wyświetlaczu LCD oraz zapisywane 
w bazie danych. Aby wykonać pomiar, będzie trzeba przyłożyć kartę, która będzie identyfikatorem 
badania. W bazie danych będą przechowywane: id badania, data badania, wynik, decyzja (czy można 
prowadzić samochód).
Dodatkowo będzie opcja administratora, który po przyłożeniu swojej karty będzie miał możliwość 
wykonania pomiaru lub akcji na bazie danych. Admin będzie miał dostęp do jej zawartości oraz będzie 
mógł wyczyścić bazę danych. Wszystkie akcje będą odbywały się poprzez interfejs na serwerze webowym 
postawionym na BeagleBone Black.


![image](https://user-images.githubusercontent.com/56175973/160384864-7193b321-e1f7-446f-ae77-ccfecb93d0e3.png)


### 1. Zakres projekt
Opis celu oraz zakresu projektu został umieszczony w karcie projektu. Szczególnie temat 
części ‘fizycznej’ został w niej w niej wyczerpany. Kilka słów należy jednak dodać do części 
softwarowej.
Dostęp do bazy danych będzie odbywał się za pomocą interfejsu na serwerze webowym 
postawionym na BeagleBone Black za pomocą technologii FLASK. Na serwerze tym 
użytkownik będzie miał dostęp do przeglądu bazy danych, dodatkowo serwer będzie 
posiadał opcje modyfikacji, czyszczenia dostępne tylko dla admina po podaniu loginu i hasła.

### 2. Schemat 


![image](https://user-images.githubusercontent.com/56175973/160385208-0d05427f-d12b-47c1-ba0d-56717a60ea6b.png)

### 3. Zdjęcie połączeń

Do realizacji projektu wykorzystaliśmy sprzęt znany nam z zajęć laboratoryjnych. Dzięki 
komunikacji Arduino oraz BeagleBoneBlack wykonaliśmy system sprawdzający ilość alkoholu 
w wydychanym przez nas powietrzu.


![image](https://user-images.githubusercontent.com/56175973/160385486-e0aa02cd-f16d-4514-ae88-bc20eec83e41.png)

### 4. Zrzuty z ekranu aplikacji 


![image](https://user-images.githubusercontent.com/56175973/160385644-0c626280-fd73-436b-8276-bd08618570f8.png)


![image](https://user-images.githubusercontent.com/56175973/160385668-49b94903-c550-4db8-a5e5-ebc0b75b3f0e.png)


![image](https://user-images.githubusercontent.com/56175973/160385698-712eaa00-f11f-41a4-976b-3881ec2db2f1.png)


![image](https://user-images.githubusercontent.com/56175973/160385729-380c9ffc-22e4-4d30-8d7f-365eaae6a8cc.png)


### 5.Podsumowując nasz projekt, udało nam się uzyskać podstawową funkcjonalność projektu. 
Zbudowaliśmy alkomat połączony z BeagleBoneBlack, który umożliwia nam swobodny 
dostęp do bazy danych pomiarów. Alkomat ten znalazłby swoje zastosowanie w tym 
momencie, ale z pewnością jest on dobrym wstępem do budowy pełnoprawnego alkomatu, 
mierzącego dokładną ilość alkoholu w wydychanym powietrzu. Dużym plusem projektu byłe 
zadecydowanie praca z BeagleBoneBlack oraz postawienie na nim serwera przy 
wykorzystaniu frameworka Flask. Wiedza oraz umiejętności nabyte podczas wykonywania 
projektu „Alkomat” niewątpliwie zbliżyły nas do bycia prawdziwymi inżynierami przemysłu 
4.0 i z pewnością okażą się bardzo przydatne w przyszłości.

