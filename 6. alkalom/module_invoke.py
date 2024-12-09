import modul_1 # teljes modul import
from modul_1 import my_func, name, my_list

# kerüljétek ezt az importot
from modul_1 import * # mindent beimportál a modul_1-ből, és a nevére hivatkozva tudod majd használni
'''
modul_1 az egy namespace -> honnan származik az objektum

Namespacek:
1. Built-in namespace: bárhonnan elérhető és a python-ba létezik az objektum
2. Global namespace  : szintén bárhonnan elérhető, a első indentation szinten van definiálva az objektum
3. Local namespace   : csak a local namespace-en érhető el -> valamilyen kódblock belselyében van definiálva

'''
# print(modul_1.name)
print(my_dict)
# Global namespace
num1 = 10
num2 = 5    

# sol = modul_1.my_func(num1, num2)
sol = my_func(num1, num2)

# modul_1.my_func = print

print(sol)

def my_func():
    # Local namespace
    temp = []
    return temp

sol = modul_1.my_func(num1, num2)