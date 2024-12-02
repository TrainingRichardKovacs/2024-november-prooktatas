"""
for loop - for ciklus

for ciklus_változó in iterable_object:
    programkód
    programkód

"""
# a páratlan számokat töröljük a my_list-ből
my_str = "Prooktatás python 2024"
my_list = [21, 35, 46, 75, 47, 36, 74, 33, 19, 41]
my_list2 = []
# print(my_list)

"""
eredeti:    [21, 35, 46, 75, 47, 36, 74, 33, 19, 41]
              0   1   2   3  4    5   6   7  8    9

módosított: [35, 46, 47, 36, 74, 19]
              0   1   2   3  4    5 
"""

for item in my_list:
    if item % 2 == 0:
        my_list2.append(item)

my_list = my_list2

# minden páratlan számot szorozzunk meg 2-vel

my_list = [21, 35, 46, 75, 47, 36, 74, 33, 19, 41]

# enumerate - minden elemhez hozzáfűzi az index értékét: (index, érték)
for idx, item in enumerate(my_list):
    if item % 2 != 0:
        my_list[idx] = item * 2

# print(my_list)
########################################################################

# adj hozzá 10 szer 5-öt a my_num-hoz

my_num = 10

for item in range(10, 99, 3):
    print(item)

for item in range(len(my_list)):
    if item % 2 != 0:
        my_list[item] = my_list[item] * 2
