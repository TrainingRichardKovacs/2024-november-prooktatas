
a = [10, 20, 30]
b = [10, 20, 30]
 
# return the location
# where the variable
# is stored
print(id(a))
 
# return the location
# where the variable
# is stored
print(id(b))
 
# returns false if the
# location is not same
print(a is b)
print(a == b)