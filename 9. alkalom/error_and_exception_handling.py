"""
Hibakezelés és kivételkezelés

2 külön dolgot jelent.
pl: raise Exception("A num2 0-volt, emiatt 0-val akartam osztani")
"""

# a fejlesztő dob hibát

num1 = 10
num2 = 6

if num2 <= 5:
    raise Exception("A num2 0-volt, emiatt 0-val akartam osztani")

my_dict = {
    "color": "black",
    "salary": "10_000"
}

# print(my_dict.get('valami'))

if my_dict.get('salary') is None:
    raise KeyError(f"The key 'valami' is not found.")

#####################################################################################################
'''
Exception handling

try:
    utasítások
exception a:
    ha a hiba van, akkor csinálok valamit
exception b:
    ha b hiba van, akkor csinálok valamit
finally:
    ez mindig lefut, függetlenül attól, hogy történt e hiba, vagy sem

    
try:
   print("I may raise an exception!")
except:
   print("I will be called only if exception occur!")
else:
   print("I will be called only if exception didn't occur!")
finally:
   print("I will be called always!")

'''

num1 = 10
num2 = 1

try:    
    if num2 <= 5:
        raise Exception("A num2 túl kicsi")
    print("almafa")
    # raise Exception("valami")
except KeyError as k_err:
    print(k_err)
except ZeroDivisionError as e:
    print(e)
except Exception as err:
    print(f"Hiba van: {err}")
else:
    print("almafa")
finally:
    print("Ez mindig lefut")

########################################################
def my_debug_decor(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as err:
            print(f"Error Occured: {err}")
            return err
    return wrapper


@my_debug_decor
def my_func(num1, num2):
    return num1 / num2

sol = my_func(10, 0)

print(sol)