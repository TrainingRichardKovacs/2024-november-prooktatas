"""
Classmethod - osztály metódus

1. Alternatív inicializálással akarunk az osztályból egy példányt létrehozni
2. Osztályszintű adatokat akarod elérhetővé tenni
3. Factory metódus: Amikor egy osztályhoz többféleképpen is létre szeretnénk hozni objektumokat,
    akkor factory metódust használnuk

"""

class Person:
    salary = 10_000

    # self azt jelenti, hogy a példányosított objektumhoz tartozik az attributum
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test_func(self, param1):
        print(param1)

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Person("Pista", 54)
        return cls(name, 2025 - birth_year)
    
    @classmethod
    def get_person_salary(cls):
        return cls.salary



person1 = Person("Pista", 54)

person1.test_func('almafa')

person2 = Person.from_birth_year("Karcsi", 1965)

print(person2.get_person_salary())
print(Person.get_person_salary())
print(person2.salary)
print(Person.salary)

###################################################################

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_square(cls, side_length):
        # return Rectangle()
        return cls(side_length, side_length)



    
t1 = Rectangle(10, 20)
t2 = Rectangle.from_square(15)

print(t1.height, t1.width)
print(t2.height, t2.width)