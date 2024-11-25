"""
List adattípus

my_list = ["Ricsi", "Peti", 1, 2, 3, (1, 2, 3, 4, 5), [4.5, 74, 232, "adgag"]]

A lista tulajdonságai: a lista megváltoztatható -> mutable adattípus
A lista iterable object -> iterálható, mert több elemre lehet bontani -> slice-olható

Lista műveletek:
1. A listához tudsz hozzáadni elemet
2. A listából tudsz elvenni elemet
3. A listában lévő elemeket tudod módosítani
4. Listákat tudsz összevonni
5. A listát lehet üríteni

"""

my_list = []

"""
Elemek hozzáadása listához

"""

# Egyszerre 1 elemet
my_list.append("Pista")
my_list.append(1)

# Több elem hozzáadása
my_list.extend(["Ricsi", "Józska", "Karcsi"])

# megadott helyre történő elem hozzáadás
# ez költséges, mert egy jó részét újra struktúrálja a listának
my_list.insert(1, "kiskutya")

##########################################################################################
"""
Elemek törlése listából

"""
my_list = [1, 2, 2, 3, "Ricsi", "Pisti", "Karcsi"]

# Index mentén való törlés
my_list.pop(4)
del my_list[-2]

# Érték alapú törlés
my_list.remove(2)

# teljes lista ürítése
my_list.clear()

my_list = []

# print(my_list)

############################################################
"""
Listák összevonása

"""

my_list = [1, 2, 2, 3, "Ricsi", "Pisti", "Karcsi"]
my_list2 = [5, 6, 7]

sol = my_list + my_list2

sol = []
sol.extend(my_list)
sol.extend(my_list2)

# packing and unpacking
# unpacking
sol = [*my_list, *my_list2]

print(sol)