# 1. feladat:

nev = "Anna"
eletkor = 25

sol = f"{nev} {eletkor} éves"

########################
# 2. feladat
termek = "táska"
ar = 5000
#Elvárt eredmény: "A(z) táska ára 5000 forint."

sol = f"A {termek} ára {ar} forint"


# 3. feladat:

nev = "Béla"
eletkor = 34
varos = "Budapest"
# Elvárt eredmény: "Béla 34 éves és Budapest-ben lakik."
sol = f"{nev} {eletkor} éves és {varos}-en lakik"
#

#4. feladat:

szamok = [1, 2, 3, 4, 5, 6]

# print(szamok[0:3])
# Elvárt eredmény: [1, 2, 3]

szavak = ["alma", "körte", "szilva", "barack"]

#print(szavak[-2:])
#print(szavak[-2::])
#print(szavak[-2::1])
#Elvárt eredmény: ["szilva", "barack"]

betuk = ["a", "b", "c", "d", "e", "f"]
#Elvárt eredmény: ["a", "c", "e"]
# print(betuk[::2])
# print(betuk[0::2])

# osszefuzés

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = []

sol = lista1 + lista2
lista3.extend(lista1)
lista3.extend(lista2)
sol2 = [*lista1, *lista2]

# print(lista3)
# print(sol)
# print(sol2)

eredeti_lista = ["piros", "kék", "zöld"]
uj_elem = ["sárga"]
# Elvárt eredmény: ["piros", "kék", "zöld", "sárga"]

lista3 = []
sol = eredeti_lista + uj_elem
lista3.extend(eredeti_lista)
lista3.extend(uj_elem)
sol2 = [*eredeti_lista, *uj_elem]

# print(lista3)
# print(sol)
# print(sol2)
# print(sol)

####################################################################
# Feladat: Készíts egy listát, amely két meglévő lista első két-két elemét tartalmazza.
#Input:
lista1 = [10, 20, 30]
lista2 = [40, 50, 60]

# print(type(lista1[:2]))
sol = lista1[:2] + lista2[:2]
sol2 = [*lista1[:2], *lista2[:2]]

sol3 = []
sol3.extend(lista1[:2])
sol3.extend(lista2[:2])

# print(sol)
# print(sol2)
# print(sol3)

my_str = "[10, 20, 40, 50]"
my_str = my_str[1:-1]
my_str = my_str.split(', ')
# my_str = "almafa"
# print(my_str)
my_list = list(my_str)
# print(my_list)

######################################

#Feladat: Adj hozzá egy új kulcs-érték párt egy meglévő dictionary-hez.
#Input:
adatok = {"név": "Gábor", "kor": 28}
uj_kulcs = "város"
uj_ertek = "Debrecen"
#Elvárt eredmény: {"név": "Gábor", "kor": 28, "város": "Debrecen"}

adatok[uj_kulcs] = uj_ertek

# print(adatok)

#Feladat: Módosíts egy meglévő kulcs értékét egy dictionary-ben.
#Input:
diak = {"név": "Zsófi", "osztály": 10, "pontszám": 85}
kulcs = "pontszám"
uj_ertek = 90
#Elvárt eredmény: {"név": "Zsófi", "osztály": 10, "pontszám": 90}

diak[kulcs] = uj_ertek
diak.update({kulcs:uj_ertek})
# print(diak) 

#Feladat: Egy meglévő dictionary-be adj hozzá két új kulcs-érték párt egyszerre.
#Input:
profil = {"név": "Anna"}
uj_adatok = {"kor": 22, "ország": "Magyarország"}
#Elvárt eredmény: {"név": "Anna", "kor": 22, "ország": "Magyarország"}

profil.update(uj_adatok)

# print(profil)

#############################################
#Feladatok:
#Feladat: Döntsd el, hogy egy szám pozitív, negatív, vagy nulla, és írd ki a megfelelő üzenetet.
#Input:
szam = -5
#Elvárt eredmény: "A szám negatív."

if szam > 0:
    print("A szám pozitív.")
elif 0 > szam:
    print("A szám negatív.")
else:
    print("A szám 0.")

#####################################################################

# Feladat: Egy hőmérsékleti érték alapján állapítsd meg, hogy hideg, kellemes vagy meleg van.
# Input:
homerseklet = 25.00000001
# Feltételek:
# Hideg: < 15
# Kellemes: 15–25
# Meleg: > 25
# Elvárt eredmény: "Kellemes az idő."

if homerseklet < 15:
    print("hideg")
elif homerseklet >= 15 and homerseklet <= 25:
    print("kellemes")
else:
    print("meleg")

#################################################################################################

if homerseklet > 25 :
    print("Meleg az idő.")
elif homerseklet < 15 :
    print("Hideg az idő.")
else:
    print("Kellemes az idő.")

#################################################################################################
# Feladat: Állapítsd meg, hogy egy diák átment-e a vizsgán (>=50 pont), vagy megbukott.
# Input:
pontszam = 50
# Elvárt eredmény: "A diák megbukott."

if pontszam >= 50:
    print("Átment")
else:
    print("Megbukott")