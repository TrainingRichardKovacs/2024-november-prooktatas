"""
Function - függvények

def function_name(opcionális_paraméter_lista):
    utasítások
    elágazások
    ciklusok
    stb.
    opcionális return -> opcionális visszatérési érték

nevezéktan: a függvények kisbetűsek, _ karakterrel elválasztottan adjunk nevet a függvényeknek
            a függvény neve legyen beszédes


Általános tudnivalók:
A függvény definíciója felfogható egyfajta "tervrajznak".
A függvények fejlesztésének egyik célja,
    DRY principle - Don't Repeat Yourself
    -> hogy elkerüljük a kód ismétléseket 
        -> ugyan arra a feladatra ne fejlesszünk 1-nél több megoldást
    -> a megoldásaink bárhol használhatóak legyenek

    -> komplex logigát elrejtsük a felhasználó elől
    -> valamilyen input adatra, valamilyen output-ot generáljon nekem a függvény
        -> ezt az output-ot visszaadjahatja -> visszatérési értéknek
        -> nem adja vissza, hanem más helyen tárolja majd le az output-ot

A python megengedi, hogy létező függvényeket újradefiniáljunk.
Ebben az esetben a definíció után meghívott függvény minden esetben az új működést fogja végrehajtani.



"""

# print("Hello világ!")

def hello_world():
    print("Hello world")

# függvény initializálása
# függvény példányosítása
# függvény meghívása
# hello_world()

###########################################################

"""
BE AWARE!!

A Python megengedi azt, hogy felüldefiniálj meglévő nevű objektumokat.
Onnantól kezdbe abban az adott fileban, az átnevezett objektum űgy fog működni, ahogy lefejlesztettük.

print("Kacsa")
print(3+2)

def enumerate():
    print(3+2)

enumerate()

my_list = [1, 2, 3, 4, 5]

for idx, item in enumerate(my_list):
    print(item)

"""
###################################################################
# függvény prototípus
"""
pass és a ... -> üres utasítás

"""
def add_numbers():
    ...

def add_numbers():
    pass

###################################################################
"""
Függvény paraméterei - függvény input adatai | input paraméterei

def add_numbers(num1, num2):
    print(num1 + num2)

A fent definiált függvény paraméterei kötelező paraméterek. A függvény példányosításakor ezeknek a paramétereknek értéket
kell adnunk.

add_numbers(10, 20) -> ez a fajta függvény hívás a pizíció alapú paraméterátadás -> positional argumentum
add_numbers(num1=50, num2=60) -> keyword-argumentum 
"""

def add_numbers(num1, num2):
    print(num1 + num2)

# add_numbers(10, 20)
# add_numbers(num1=50, num2=60)
# add_numbers(num2=50, num1=60)
###################################################################################
"""
Függvény visszatérési értéke:
#########################################################
Minden függvénynek van visszatérési értéke, függetlenül attól, hogy rendelkezünk e a visszatérési értékkel.
Ha nincs return utasítás, akkor MINDEN ESETBEN A None érték lesz a visszatérési érték

def add_numbers(num1, num2):
     print(num1 + num2)

my_val = add_numbers(10, 20)

#########################################################

"""

def add_numbers(num1, num2):
    return num1 + num2

add_numbers(10, 20)
sol = add_numbers(10, 20)
sol1 = add_numbers(num1=50, num2=60)
sol2 = add_numbers(num2=50, num1=60)

# print(sol)
# print(sol1)
# print(sol2)

def my_func():
    # vesszővel való felsorolást a python tuple-be csomagolva adja vissza
    return 1, 2, 3, 4, 5, 6, 7

sol = my_func()

# print(sol)

################################################################################################################
'''
Multiple parameter handling with *args, **kwargs


@function overloading
--------------------------------------------------------
PL/SQL programozásnyi nyelvben

function my_function(age int);
function my_function(age int, name varchar);

my_function(34);
my_function(34, "Ricsi");
--------------------------------------------------------

*args - positional argumentumok gyűjtője -> tuple-ben fogja becsomagolni a positional argumentumokat -> ezt a * okozza
**kwargs - keyword-argumentumok gyűjtője -> dictionary-be fogja becsomagolni a keyword-agumentumokat, mint kulcs-érték párok -> ezt a ** okozza

if type(valtozo) == str -> string
if type(valtozo) == list -> lista
if type(valtozo) == dict -> dictionary
if type(valtozo) == tuple -> tuple
if type(valtozo) == int -> integer
if type(valtozo) is None -> None

'''


def my_func(*args):
    print(args)

# my_func(10, 20, "Ricsi", (1, 2, 3), ["almafa", "Karcsi"])
# my_func(10, 20)

def my_func(**kwargs):
    print(kwargs)


# my_func(age=34, name="Ricsi", job="Data Engineer")

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)


# my_func(10, 20, "Ricsi", age=34, job="Data Scientist")
# my_func(10, 20, "Ricsi")
# my_func(age=34, job="Data Scientist")
# my_func()

###########################################################################################################
'''
Argumentumok kezdőértéke

'''

def my_func(num1: int=10, num2: int=20)-> int:
    return num1 + num2

sol = my_func(5, 6)
sol = my_func(num2=10_000, num1=400)

# print(sol)

def my_func(temp=[]):
    print(temp)

# my_func([1, 2, 3])

###########################################################

'''
Paraméter átadás:
1. Érték szerinti
2. Referencia szerinti

'''
m_list = [item for item in range(10)]

def my_func(my_list: list, value):
    temp = []
    temp.extend(my_list)
    temp.append(value)
    return temp

sol = my_func(m_list, "almafa")

# print(m_list)
# print(sol)

########################################
# 1. Érték szerinti
my_str = "almafa"

def my_func(m_str):
    my_str = m_str + " " + " hordó"
    print(my_str)

my_func(my_str)
print(my_str)

