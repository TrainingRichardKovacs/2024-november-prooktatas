"""
Stringek

A stringek értéke megváltoztathatatlan -> immutable -> immutable adattípus
A string felbontható karakterekre -> alma -> a, l, m, a -> részekre bontható
    -> iterálható objektumok -> iterable object
(ciklus)
"""

my_str = "ez egy string"
my_str2 = 'ez egy másik string'

my_str = "ez egy teljesen új string"

name = "Ricsi"

#############################################

my_str = "ricsi"

#my_str = my_str.capitalize()
#my_str = my_str.capitalize()
my_str = my_str.replace('r', 'R')

#############################################
"""
Slicing művelet

my_str = "almafa"

# slicing művelet formai leírása
my_str[from:to:lépték_mértéke]
my_str[kezdő_index:ameddig:emekkora_ugrásokkal]
"""
# stringek hossza: len() függvény

my_str = "almafa"

hossz = len(my_str)

# A string első karakterét szeretném kiíratni
sol = my_str[0]

# Az utolsó karakter szeretném kiíratni
sol = my_str[-1]

# Minden második karaktert írjunk ki
my_str = "Ez hagymásbab? Nem, krumplis hal."

# a teljes stringet visszaadja
sol = my_str[:]
# az elejétől, a végéig, egyesével
sol = my_str[::]
sol = my_str[0::1]

sol = my_str[0::2]
sol = my_str[::5]

# írassuk ki a hagymásbab szót
# 3-as indextől a teljes stringet
sol = my_str[3:13]
# HU24 12345678-12345678-12345678

# Fordítsuk meg a stringet
my_str = "Ez hagymásbab? Nem, krumplis hal."
my_str = "indul a görög aludni"

sol = my_str[::-1]

################################################
# Egyéb műveletek stringekkel

# Stringek összevonása

firstname = "Charlize"
lastname = "Theron"
# + jel stringek esetében összefűzést -> string concatenation-t 
full_name = firstname + " " + lastname

################################################################

firstname = "Charlize"
lastname = "Theron"
full_name = firstname + " " + lastname + " "

print(full_name * 5)
