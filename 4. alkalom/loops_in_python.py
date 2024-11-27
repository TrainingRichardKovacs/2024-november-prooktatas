"""
2 féle ciklus:

while loop - hátultesztelős ciklus
for loop - előltesztelős ciklus

Mire használjuk frekventáltan a while ciklust:
event alapú működéseknél használjuk, amikor bizonyos eseményeket, történéseket, állapotokat ellenőrzöl
és ezek határására vagy folytatódik a futás, vagy leáll a futás

pl. Desktop applikáció, játékok, vagy azok a programok, amelyek ilyen "örökké kellene futnia"

For ciklus:
iteráljunk valamilyen iterálható objektumon és valamilyen műveletet / vizsgálatot elvégezzünk.

while logikai_vizsgálat_amíg_igaz:
    programkód
    programkód

break - kilépünk a ciklusból
"""
 
my_num = 10

while my_num > 0:
    if my_num == 5:
        break
    if my_num % 2 != 0:
        my_num -= 1
        continue
    print(f"ez a {my_num}")
    # my_num = my_num - 1

    my_num -= 1