'''
Decorator functions - decoration -> decorator pattern

A decorator függvény plusz tulajdonságot képes hozzáadni egy függvény működéséhez
anélkül, hogy változtatna annak eredeti működésén

Use-casek: mikor célszerű használni a decoratorokat
- logolás
- debugolás
- cachelés
- Authorization - jogosultság kezelés
- Authentication - belépés
- hibakezelés
- Input validation
- futási idő mérés

Amikor pl. webframework-öket illetve OOP-t fogsz használni

'''

def my_func():
    print("Hello world")

# my_func() # () kiadása maga a példányosítás a függvények esetében

# a függvény referenciájának
my_val = my_func
# my_val()
####################################
def my_func(func, num1, num2):
    print(f"if num1 > num2? {num1>num2}")
    return func(num1, num2)

def add_numbers(num1, num2):
    return num1 + num2

# sol = my_func(add_numbers, 100, 15)

#########################################################################################
def time_it(func):
    def wrapper(*args, **kwargs):
        import time # local import -> ha máshol a file-ban nem kell ezt a libraryt használni -> gyorsabb lesz a kódod
        start_dt = time.time()
        # ide tudsz adni új logikát
        func(*args, **kwargs)
        # illetve ide
        print(f"it took {time.time() - start_dt} sec")
    return wrapper


@time_it
def count_list_elements(len_of_list):
    my_list = [item for item in range(len_of_list)]

    count = 0
    for idx, item in enumerate(my_list):
        if item % 2 == 0:
            my_list[idx] = item ** 2
        count += 1

@time_it
def delete_items_from_list(len_of_list):
    my_list = [item for item in range(len_of_list)]
    temp = []
    for idx, item in enumerate(my_list):
        if item % 3 != 0:
            temp.append(item)

@time_it
def my_func(num1, num2, num3):
    import time
    time.sleep(5)

count_list_elements(1_000_000)
delete_items_from_list(1_000_000)
my_func(1, 2, 3)
# egy módja a decorator használatnak
# time_it(count_list_elements)
# time_it(delete_items_from_list)
