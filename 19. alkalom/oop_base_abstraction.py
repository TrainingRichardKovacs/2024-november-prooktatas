"""
OOP - Object Oriented Programming

class-okba fogjuk szervezni a kódunkat
Nagyon hasonló a függvények kódszervezésére, viszont
rengeteg olyan plusz lehetőséget ad nekünk a class, mint eszköz
amit egy függvény esetében nem tudunk elérni.

Camel Case - MyClass - PostgresConnectionHelper


"""

class MyClass:
    pass

# objektum példányosítása
# a MyClass-ból létrehozok egy példányt
my_obj = MyClass()
my_obj2 = MyClass()

"""
Abstraction - Absztrakció: elrejtem a classban a logikát, én csak használni akarom a logikát
                           elrejtem a classban a classból példányosított objektum működési logikáját

"""

class Human:

    """
        __init__: 
        minden példányosításnál 1szer lefut automatikusan
        az __init__ metódus egy double-underscore vagy dunderscore method, magic method 
        az __init__ metódus szolgál arra, hogy paramétereket lehessen a class-nak példányosításkor átadni
        az __init__ metódusra nincs minden esetben szükség - opcionális
        az __init__ metódust másnével konstruktornak nevezzük
        az __init__ metódus első paramétere mindig a self
        az __init__ metódusban tudunk instance változókat létrehozni

        a self szó -> a példányosított objektumot jelenti, maga az instance
        self.valtozo -> instance változó
    """

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        self.salary = 10_000
        self.nagyon_hosszu_valtozo_name = "almafa"
    
    def hello_world(self):
        print(f"Hello {self.name}")

    def _eye_color(self):
        print(self.eye_color)


arnold = Human(name="Arnold", age=45, job="Data Engineer")
stallone = Human(name="Stallone", age=75, job="Actor")

arnold.hello_world()
stallone.hello_world()

arnold.salary = 15_000

# létre tudsz hozni olyan instance változót, ami nincs deklarálva az __init__ metódusban
arnold.eye_color = "brown"

arnold._eye_color()
##############################################################