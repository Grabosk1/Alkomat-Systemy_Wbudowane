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


###1. Zakres projekt
Opis celu oraz zakresu projektu został umieszczony w karcie projektu. Szczególnie temat 
części ‘fizycznej’ został w niej w niej wyczerpany. Kilka słów należy jednak dodać do części 
softwarowej.
Dostęp do bazy danych będzie odbywał się za pomocą interfejsu na serwerze webowym 
postawionym na BeagleBone Black za pomocą technologii FLASK. Na serwerze tym 
użytkownik będzie miał dostęp do przeglądu bazy danych, dodatkowo serwer będzie 
posiadał opcje modyfikacji, czyszczenia dostępne tylko dla admina po podaniu loginu i hasła.

###2. Schemat 


![image](https://user-images.githubusercontent.com/56175973/160385208-0d05427f-d12b-47c1-ba0d-56717a60ea6b.png)

###3. Zdjęcie połączeń

Do realizacji projektu wykorzystaliśmy sprzęt znany nam z zajęć laboratoryjnych. Dzięki 
komunikacji Arduino oraz BeagleBoneBlack wykonaliśmy system sprawdzający ilość alkoholu 
w wydychanym przez nas powietrzu.


![image](https://user-images.githubusercontent.com/56175973/160385486-e0aa02cd-f16d-4514-ae88-bc20eec83e41.png)


