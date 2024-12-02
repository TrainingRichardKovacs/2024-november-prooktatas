"""
Generator comprehension

Egy iterator object ami LAZY EVALUATION-t használ.
Lazy evaluation azt jelenti, hogy nem értékeli ki az elemeket -> nem tárolja a memóriában
csak akkor kéri le az aktuális elemet, amikor te azt ténylegesen használni akarod
---> Ez memória hatékony, cserébe viszont lassú



pl my_gen = (item for item in range(100) if item % 3 == 0)

Nem lehet slice-olni. Nincs hossza.
A generator objecten való iterálásnál az iterator számon tarja, hogy hol áll jelenleg az iterálás.
Túl lehet iterálni a next függvénnyel -> célszerű ciklusokkal bejárni

"""

my_list2 = [item for item in range(1_000_000) if item % 3 == 0]

my_gen = (item for item in range(1_000_000) if item % 3 == 0)

# print(next(my_gen))
# print(next(my_gen))


# for item in my_gen:
#     print(item)

import sys

print(sys.getsizeof(my_list2))
print(sys.getsizeof(my_gen))