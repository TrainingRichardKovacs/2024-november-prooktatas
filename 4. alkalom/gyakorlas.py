"""
Sziasztok!
Itt van egy pár gyakorló feladat.
Jó munkát!

1. típus: f-string gyakorlása
Feladatok:
Feladat: Készíts egy f-stringet, amely megjeleníti egy név és életkor alapján a következőt: "{név} {életkor} éves."
Input:
nev = "Anna"
eletkor = 25
Elvárt eredmény: "Anna 25 éves."
Feladat: Hozz létre egy f-stringet, amely egy termék árát és nevét kombinálja, így: "A(z) {termek} ára {ar} forint."
Input:
termek = "táska"
ar = 5000
Elvárt eredmény: "A(z) táska ára 5000 forint."
Feladat: Egy személy nevét, korát és városát kombináld egy mondatba, például: "{nev} {eletkor} éves és {varos}-ban/-ben lakik."

Input:
nev = "Béla"
eletkor = 34
varos = "Budapest"
Elvárt eredmény: "Béla 34 éves és Budapest-ben lakik."
2. típus: Lista műveletek (slicing)
Feladatok:
Feladat: Írd ki az első három elemet a listából slicing segítségével.
Input:
szamok = [1, 2, 3, 4, 5, 6]
Elvárt eredmény: [1, 2, 3]
Feladat: Hozz létre egy új listát, amely csak a lista utolsó két elemét tartalmazza.
Input:
szavak = ["alma", "körte", "szilva", "barack"]
Elvárt eredmény: ["szilva", "barack"]
Feladat: Írd ki minden második elemet a listából slicing segítségével.
Input:
betuk = ["a", "b", "c", "d", "e", "f"]
Elvárt eredmény: ["a", "c", "e"]
3. típus: Lista összevonás ciklusok nélkül
Feladatok:
Feladat: Fűzz össze két listát úgy, hogy az eredményben az összes elem szerepeljen.
Input:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
Elvárt eredmény: [1, 2, 3, 4, 5, 6]
Feladat: Adj hozzá egy új elemet egy meglévő listához lista-összevonás segítségével.
Input:
eredeti_lista = ["piros", "kék", "zöld"]
uj_elem = ["sárga"]
Elvárt eredmény: ["piros", "kék", "zöld", "sárga"]
Feladat: Készíts egy listát, amely két meglévő lista első két-két elemét tartalmazza.
Input:
lista1 = [10, 20, 30]
lista2 = [40, 50, 60]
Elvárt eredmény: [10, 20, 40, 50]
4. típus: Dictionary műveletek
Feladatok:
Feladat: Adj hozzá egy új kulcs-érték párt egy meglévő dictionary-hez.
Input:
adatok = {"név": "Gábor", "kor": 28}
uj_kulcs = "város"
uj_ertek = "Debrecen"
Elvárt eredmény: {"név": "Gábor", "kor": 28, "város": "Debrecen"}
Feladat: Módosíts egy meglévő kulcs értékét egy dictionary-ben.
Input:
diak = {"név": "Zsófi", "osztály": 10, "pontszám": 85}
kulcs = "pontszám"
uj_ertek = 90
Elvárt eredmény: {"név": "Zsófi", "osztály": 10, "pontszám": 90}
Feladat: Egy meglévő dictionary-be adj hozzá két új kulcs-érték párt egyszerre.
Input:
profil = {"név": "Anna"}
uj_adatok = {"kor": 22, "ország": "Magyarország"}
Elvárt eredmény: {"név": "Anna", "kor": 22, "ország": "Magyarország"}
5. típus: if-else gyakorló feladatok
Feladatok:
Feladat: Döntsd el, hogy egy szám pozitív, negatív, vagy nulla, és írd ki a megfelelő üzenetet.
Input:
szam = -5
Elvárt eredmény: "A szám negatív."
Feladat: Egy hőmérsékleti érték alapján állapítsd meg, hogy hideg, kellemes vagy meleg van.
Input:
homerseklet = 25
Feltételek:
Hideg: < 15
Kellemes: 15–25
Meleg: > 25
Elvárt eredmény: "Kellemes az idő."
Feladat: Állapítsd meg, hogy egy diák átment-e a vizsgán (>=50 pont), vagy megbukott.
Input:
pontszam = 47
Elvárt eredmény: "A diák megbukott."

"""