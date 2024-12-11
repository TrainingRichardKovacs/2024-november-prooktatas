"""
Scope - Variable scope

A változók | objektumok láthatóságát és élettartamát határozza meg.

Szintjei:
1. Built-in scope - bárhol tudom használni a Pythonon belül
2. Global scope - az adott file-ban, akár melyik scope-on belül tudom használni az adott objektumot
3. Enclosing scope - opcionális
4. Local scope - local scope-on létrehozott objectum csak local scope-on belül használható
                 amikor a pl. függvény lefutott, akkor a local scope-jában létrehozott objektumok
                 megszűnnek létezni

"""

name = "Ricsi"

def my_func():
    # ez a local scope
    age = 40
    print(f"ez is  a name változó: {name}")

# a függvény példányosítása itt történik meg
# my_func()
##################################################################################################
'''
Függvény a függvényben
Nested function

'''

# Egy egyszerű számológép alkalmazást írjunk, ahol paraméterként
# megadunk 2 számot és a köztük lévő műveletet: +, -, *, /

def calculator(num1, num2, operand):
    # enclosing
    def add():
        # local 
        return num1 + num2

    def substract():
        return num1 - num2
    
    def power():
        return num1 * num2

    def devide():
        return num1 / num2

    if operand == '+':
        sol = add()
    elif operand == '-':
        sol = substract()
    elif operand == '*':
        sol = power()
    elif operand == '/':
        sol = devide()
    else:
        print("Nem megfelelő műveletet adtál meg")
        return None

    return sol

sol = calculator(2, 10, "+")

# print(sol)


########################################################################################################
# Global scope
age = 40

def main_function():
    # enclosing scope
    age = 15
    def inner_function():
        # local scope
        # main_function.inner_function
        nonlocal age
        age = 5 # age = age + 5
        print(age)

    inner_function()
    print(age)


if __name__ == '__main__':
    print(f"függvény futása előtt: {age}")
    main_function()
    print(f"függvény futása után: {age}")

    print()

    print(__name__)
