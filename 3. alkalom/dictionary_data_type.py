"""
Dictionary - Hashmap

Kulcs típusa bármi lehet, ami hashelhető -> hashable data types
int (Egész számok)
float (Lebegőpontos számok)
complex (Komplex számok)
bool (Logikai értékek)
str (Karakterláncok)
tuple (Ha az összes eleme is hashable)
NoneType (None az egyetlen érték)

A dictionary egy mutable adattípus - megváltoztatható
1. lehet hozzáadni kulcs-érték párokat
2. lehet törölni kulcs-érték párokat
3. lehet módosítani kulcs - érték párokat - kulcsot nem tudsz cserélni
4. lehet dictionary-ket összevonni

A dictionary az egyik leggyorsabban kereshető adattípus.
A dictionary kulcs unique - egyedi. Egy szinten, csak egy azonos nevű kulcs lehet.

my_dict = {
    "kulcs": "érték",
    "color": "black",
    "salary": 30_000,
    (1, 2, 3): "valami"
}

ez nem dictionary: my_dict = {1, 2, 3, 4} -> ez set adattípus

"""

my_dict = {
    "color": "black",
    "salary": 50_000
}

# Kulcs - érték hozzáadása
# egyszerre 1 kulcs és 1 érték
my_dict["brand"] = "Mercedes"

# több kulcs és több érték
my_dict.update({"new_key": "new_value", "title": "Mr.", "neme": "Férfi"})
# print(my_dict)
#####################################################################
# meglévő kulcs - érték pár módosítása ! directben nem tudod a kulcs nevét módosítani
my_dict = {
    "color": "black",
    "salary": 50_000
}

# egy kulcs-érték módosítás
my_dict["color"] = "purple"

# több kulcs érték módosítása
my_dict.update({"salary": 60_000})

###############################
# kulcs - érték törlése

my_dict = {'color': 'black',
            'salary': 50000,
            'brand': 'Mercedes',
            'new_key': 'new_value',
            'title': 'Mr.',
            'neme': 'Férfi'
            }


# value = my_dict.pop("neme")
my_dict.pop("neme")
temp = my_dict.popitem()

del my_dict["color"]

#########################################################################
# Dictionary-k összevonása
my_dict = {
    "color": "black",
    "brand": "mercedes",
}

my_dict2 = {
    "shop": "Budapest",
    "employee": 10
}


my_dict.update(my_dict2)
my_dict3 = {**my_dict, **my_dict2}
my_dict4 = my_dict | my_dict2
###################################################################

