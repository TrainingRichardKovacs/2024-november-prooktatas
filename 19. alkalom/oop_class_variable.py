"""
Class attributes - 
    class variable
    class method

1. a class változót az instance-on keresztül eléred
2. a class példányosítása nélkül is tudom használni. Class.class_variable



"""

class Test:
    my_class_val = "valami"

    def __init__(self):
        # instance variable
        self.val = 10

    def print_class_value(self):
        print(self.my_class_val)

    #innen folytatni
    @classmethod
    def my_classmethod(cls):
        ...

test = Test()

test.print_class_value()
print(test.my_class_val)
print(Test.my_class_val)

test2 = Test()
test2.val = 20

Test.my_class_val = "akármi"

print(test.my_class_val)
print(test2.my_class_val)

test.my_class_val = "bármi"

print(test.my_class_val)
print(test2.my_class_val)

Test.my_class_val = "nem tudom"

print(test.my_class_val)
print(test2.my_class_val)

test.my_class_val = Test.my_class_val

print(test.my_class_val)
print(test2.my_class_val)

Test.my_class_val = "tudom is én"

print(test.my_class_val)
print(test2.my_class_val)