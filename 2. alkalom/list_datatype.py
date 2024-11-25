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

################################################################################################################
# Meglévő elem módosítása

my_list = [1, 2, 3, 4, 5]

my_list[1] = "alma"
print(my_list)
##############################
# 3. elemtől minden elemet le akarok cserélni
my_list = [1, 2, 3, 4, 5]

my_list[2::1] = (10,) # tuple
my_list[2::1] = 20, 21, 22, 23, 24, 25 # ez egy felsorolás
##############################

my_list[-1] = None

my_list[1] = (10, 20, 30, 40)

# print(my_list)
# print(my_list[1][2])

#####################################################################################
# unpack utasítást

my_list = [1, 'alma', 3, 4, 5]

# 
# a, b, c = my_list[0:3] 
# *packing | a, b, c = my_list[1:] -> unpacking művelet
a, b, *c = my_list[1:] 

######################################################################################
# referencia hivatkozás listák között


my_list = [1, 'alma', 3, 4, 5]

# ez egy kétirányú referencia: ha az egyik list elemeit módosítod, akkor módosul a másik lista is
# ez alól kivétel az új értékadás - pl. my_list = [1, 2, 3]
my_list2 = my_list

my_list.append(10)
my_list2.extend("Karcsi")

my_list[-1] = "almafa"

my_list2[3:-1] = "Karcsi", "Zsolti"

#############################################################

my_tuple = [1, 2, [0, 1], "Ricsi"] 
my_tuple[2].append(10)

my_list = [1, 2, 3]

# print(id(my_list[0]))
# print(id(my_tuple[0]))
# print(id(my_tuple[2][1]))

#############################################################
temp = [10, 20]
my_tuple = (1, 2, temp)
my_list = [1, 2, 3, 4, 5, temp]

my_list2 = my_list

my_list2[-1].append(30)

print(my_tuple)
print(my_list)





