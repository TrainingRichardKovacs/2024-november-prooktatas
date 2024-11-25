"""
Tuple

my_tuple = (1, 2, 3, 4, True, False, "Ricsi")

Tuple tulajdonságai: a tuple megváltoztathatatlan -> immutable adattípus
A tuple iretable object -> iterálható -> slicing művelet használható

Mire jó a tuple?
A tuple egy memóriahatékony adattípus 
"""
my_tuple = (1, 2, 3, 4, True, False, "Ricsi")

# ez a 2 művelet: nagyon drága
print(my_tuple.count(0))
print(my_tuple.index("Ricsi"))

print(my_tuple[::-1])