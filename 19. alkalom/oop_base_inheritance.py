"""
Inheritance - öröklődés

Szülő - gyermek kapcsolatot hozunk létre az osztályok között
A gyermek osztály a szülő minden tulajdanságát örökli - tudja használni - 
A szülőtől örökölt attributumokat - változók, függvények - a gyermek osztályban felül lehet
definiálni

"""
# szülő osztály
class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hello, {self.name}")

# gyermek osztály
class Man(Human):
    
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sex = "male"

class Woman(Human):
    
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sex = "woman"


john = Man(name="John", age=23)
sarah = Woman(name="Sarah", age=43)

sarah.say_hi()
print(john.age)
john.say_hi()