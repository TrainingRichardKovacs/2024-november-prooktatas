"""
String formatting - string formázás

4. fajtája van
3-at nézünk

1. Old style formatting
2. New style formatting
3. String interpoláció
4. String template-ing - importálni kell egy library-t

Tetszőleges mennyiségő placeholdert használhattok
"""

# 1. Old style formatting: %s - python 2.x
# George most lett 40 éves

name = "George"
age = 40

# %s - egy placeholder karakter - ő csak foglalja a helyet
# %s - string, %x - hexadecimális, %f - float
#sol = "%s most lett %.3f éves" %(name, age)
sol = "%s most lett %.3f éves" 

# print(sol %(name, age))


# 2. New Style formatting
# George most lett 40 éves
name = "George"
age = 40

sol = "{akármi} most lett {a:.3f} éves".format(akármi=name, a=age)


# 3. String interpoláció - f' string
# George most lett 40 éves
person = "George"
person_age = 40

sol = f"{person:s} most lett {person_age:.3f} éves"

print(sol)
##################################################################################################

my_str = "indul a görög aludni"

# sol = my_str[0:8] + my_str[14:]
sol = f"{my_str[0:8]}{my_str[14:]}"

# my_str = my_str.replace("görög", "")

print(my_str)