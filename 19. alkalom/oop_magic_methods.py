"""
Magic Methods - double underscore methods - dunderscore methods

__method__

"""

class MyClass:

    def __init__(self):
        self.name = "Amanda"
        self.my_list = [1, 2, 3, 4, 5, 6, 7]

    def __len__(self):
        return len(self.my_list)
    
    def __del__(self):
        print("Törölték az objektet")
        del self

    def __str__(self):
        return f"{self.__class__}: {self.name} object"
    
    def __sizeof__(self):
        return 1024

import sys

test = MyClass()
test2 = 10

print(sys.getsizeof(test))

# print(len(10))
test.my_list.append("Ricsi")
print(len(test))

del test


