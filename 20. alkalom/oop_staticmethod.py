"""
Staticmethod

Definició: Olyan Utility functionök (segédfüggvényeknek), amelyek nem módosítják sem az osztály 
            sem az instance állapotát.

Tulajdonság: Ha egy függvénynek nincs szüksége sem az osztály sem a példány változóira : self, cls akkor
        az egy staticmethod

        Ha a függvény az osztályhoz kapcsolódik, de nem szükséges példányosítani az osztályt a meghíváshoz
        akkor az egy staticmethod

A staticmethod nem tudja elérni a self-es attributumokat - az instance attributumokat
A staticmethod nem tudja elérni a class attributumokat sem.
"""

class MathUtils:
    test_class_var = "kacsa"

    def __init__(self):
        self.test_variable = "almafa"

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def add_2(a, b):
        return a + b


test = MathUtils()

print(test.add(1, 2))
print(MathUtils.multiply(0, 10))
