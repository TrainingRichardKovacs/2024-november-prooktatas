"""
3 -as szabály - 3 lépés:

1. Megnyitjuk a file-t valamilyen megnyitási formával: vannak megnyitási módok, amelyek
    azt befolyásolják, hogy milyen típusú műveletet tudunk az adott file-on elvégezni
    pl: mode="r" -> read -> csak olvasásra megnyitott állapot -> tudom használni a file tartalmát, de 
    nem tudom módosítani
2. Elvégezzük a file-on a szükséges műveleteket: 
    pl. adat kinyerés, file-ba írás, file törlés stb., file tartalmának módosítása
3. lezárjuk a megnyitott file-t

built-in function: open()

egy-két speciális karakter: \n -> sortörés - új sor
                            \t -> tabulátor

.read() -> stringként olvassa ki az adatot

"""
# file_path = "C:/WORK/Prooktatas/2024-november/8. alkalom/mai_anyag.txt"
file_path = r"C:\WORK\Prooktatas\2024-november\8. alkalom\mai_anyag.txt"
# file_path = r"C:\WORK\Prooktatas\2024-november\.vscode\launch.json"

# az open nem tölti be a memóriába a megnyitott file-t
my_file = open(file_path, "r", encoding="utf-8")
# a .read() a file teljes tartalmát olvassa ki és tárolja a memóriába
data = my_file.read()

my_file.seek(0,0)
data2 = my_file.readlines()

print(data)
print(data2)

my_file.close()


##################################################
# file írása: mode="w"
"""
mode = "w" -> ha nem létezik a file, akkor létrehoz egy üres file-t
           -> ha már létezik a file, akkor felülírja egy üres file-al

"""

file_path = r"C:\WORK\Prooktatas\2024-november\8. alkalom\test_file.txt"
my_file = open(file_path, "w", encoding="utf-8")
my_file.write(data)
my_file.close()

# contextusmanager - következő órán
with open(file_path, "w", encoding="utf-8") as f:
    f.write(data)