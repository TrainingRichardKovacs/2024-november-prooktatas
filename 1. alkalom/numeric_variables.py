"""
Változó
(az  = jel, az értékadás operátor)
valtozo_neve = valtozo_értéke

Egy változó bármennyiszer kaphat értéket
Ebben az esetben az utoljára adott érték lesz az ő végleges értéke

"""

'''
num = 10
num2 = 10

num = 20
num2 = 10


print(id(num))
print(id(num2))

'''

num = 10
'''
Referencia létrehozás, de ez csak egyirányú referencia

Egyirányú referencia: num2 = num -> num2 rá mutat a num-ra, ez az egy irány van
                                 -> ha a num értéke változik, akkor a num2 nem követi tovább, hanem az eredeti értékét
                                    fogja a num-nak vinni magával

'''
num2 = num

my_salary = 50_000
my_salary = my_salary * 1.5

'''
Szám típusok fajtái:

num = 10 -> egész szám -> integer
num = 3.14 -> tizedes tört -> float (lebegőpontos szám)

num = 3j + 2 -> complex szám
'''

'''
Dinamyc typing
Dinamikusosan típusos nyelv: a változó létrehozásakor nem kell megadnod annak típusát
                            -> a Python futási időben "találja" ki a változó típusát
                            -> egy változó bármikor kaphat akármilyen típusú értéket (Python engedélyezett)

= -> értékadás operátor
'''
num = 10
num = 3.14
num = 3j + 2

##########################################################################

# számokat lehet összeadni, kivonni, szorozni, osztani, maradékos osztást - operátorokkal

# type hinting -> sintactic sugar -> cukrozás
num: int = "Ricsi"

num = 10.4
num2 = 1

# összeadás
sol = num + num2
print(sol)
# kivonás
sol = num - num2
print(sol)
# szorzás
sol = num * num2
print(sol)
# osztás
'''
valódi osztás:
int / int -> float ;
float / float -> float,
float / int -> float
'''
sol = num / num2  
print(sol)

"""
num = 10.4
num2 = 1


C#

float num = 10.4;
int num2 = 1;
float sol;

sol = num + num2;


"""

############################################
# maradékor osztás: a maradékot adja vissza

num = 5
num2 = 2

# maradékos osztás
sol = num % num2
# egész osztás -> azt adja vissza, hogy hányszor van meg a szám de csak az egész részét, a tizedes jegyeket lehagyja
sol = num // num2
print(sol)

