"""
If statement - Elágazások

if (logikai_vizsgálat, ha teljesül):
    művelet
elif (logikai_vizsgálat, ha teljesül):
    művelet
elif (logikai_vizsgálat, ha teljesül):
    művelet
elif (logikai_vizsgálat, ha teljesül):
    művelet
else:
    művelet

indentáció - indentation
alapesetben 1 indentációs szint, az 4 space vagy 1 tabulátor

"""
# Adja össze a 2 számot, 
#   ha az első szám nagyobb, mint a másik, 
#   ha az első szám kisebb mint a második, akkor vonja ki őket egymásból
#   egyébként meg szorozzat őket össze egymással

num1 = 100
num2 = 20

print(num1 > num2)

# if num1 > num2 :
#     print(num1 + num2)
# elif num2 > num1:
#     print(num1 - num2)
# else:
#     print(num1 * num2)
############################################################################
if num1 > num2 :
    print(num1 + num2)

if num2 > num1:
    print(num1 - num2)


print("az if után vagyok")

