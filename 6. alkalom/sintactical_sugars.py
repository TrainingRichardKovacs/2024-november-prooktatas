'''
Type Hint
def my_func(my_num1: int, my_num2: int)-> int:
    return my_num1 + my_num2

'''
# 2 számot adjunk össze
def my_func(my_num1: int, my_num2: int)-> int:
    """
    This function is add two numbers

    Type Hint
        def my_func(my_num1: int, my_num2: int)-> int:
            return my_num1 + my_num2
    """
    return my_num1 + my_num2

sol: list = my_func("Ricsi", "Petra")

sol = print(sol)

print(sol)