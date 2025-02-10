"""
Polimorfizmus - többalakuság



"""

my_list = [1, 2, 3, 4, 5]
my_str = "dgsdghsdgaydhf"

print(len(my_list))
print(len(my_str))

# Parent Class
class Dog:
    def sound(self):
        print("dog sound")  # Default implementation

# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")  # Overriding parent method

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")  # Overriding parent method


dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound() 