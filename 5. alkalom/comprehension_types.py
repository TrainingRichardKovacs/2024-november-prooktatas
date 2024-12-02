"""
Comprehension műveletek

List comprehension: [ami_az_append_be_kerül for ciklus ha_van_akkor_az_if_else_ag]
Dict comprehension
generator comprehension

"""
my_list = []

for item in range(100):
    if item % 3 == 0:
        my_list.append(item)

#print(my_list)

# list comprehension
my_list2 = [item for item in range(100) if item % 3 == 0]

######################################################################################
# dictionary comprehension

my_dict = {}

for item in range(100):
    key = f"{item}_item"
    my_dict[key] = item * 2.54


my_dict2 = {f"{item}_item":item * 2.54 for item in range(100)}

# print(my_dict == my_dict2)

my_int = 10

my_str = str(my_int)

#########################################################################