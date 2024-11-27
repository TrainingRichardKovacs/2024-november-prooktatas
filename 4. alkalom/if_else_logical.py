"""
and művelet: ha az and-nél használt minden feltétel igaz - True - akkor fog igazzal visszatérni

Best practice:
A legerősebb feltétellel kezdjük az if statement-et,
mert ha az hamis, akkor nem nézi tovább a többi logikai vizsgálatot

or művelet - vagy művelet
Ha bármelyik feltétel igaz - True - , akkor igaz lesz a kiértékelés

"""

my_str = "Ricsi"
# my_list = ["Karcsi", "Pisti", "Ricsi", "Peti"]
my_list = ["Ricsi", "Peti"]

# HA a Ricsi benne van a listában és a lista legalább 2 elemű
# akkor írjuk ki, hogy Ricsi benne van a listában

if (my_str in my_list) and (len(my_list) > 2):
    print("Benne van")

##########################################

my_dict = {
    "color": "black",
    "salary": 10_000,
    "brand": "Volvo"
}

# Ha a color black és a brand meg van adva
"""
dictionary - ha egy kulcsot akarsz ellenőrizni, hogy benne van e a dictionary-be

my_dict = {
    "color": "black",
    "salary": 10_000,
    "brand": "Volvo"
}

# csak az első szinten
my_dict.get(kulcs_neve) -> ha benne van, akkor a kulcs értékét adja vissza, ha nincs benne, akkor egy None-t

if 10:
    print("a számok True értéket jelentenek, kivétel a 0")

if "Volvo":
    print("a stringek True értéket jelentenek")

if (10,):
    print("A tuple, ha nem üres, akkor True, ha üres, akkor False")

if [10]:
    print("A lista, ha nem üres, akkor True, ha üres, akkor False")

if {"kulcs": "érték"}:
    print("A dict, ha nem üres, akkor True, ha üres, akkor False")

if None: -> a None az mindig False

"""
my_dict = {
    "color": "black",
    "salary": 10_000,
    "brand": "Volvo"
}


if my_dict.get("cica") and my_dict['color'] == "black":
    print("Valami")


my_dict = {
    "child3" : {
        "child1" : {
            "name" : "Emil",
            "year" : 2004
        },
        "child2" : {
            "name" : "Tobias",
            "year" : 2007
        },
        "child3" : {
            "name" : "Linus",
            "year" : 2011
        }
    }
}

# print(my_dict['child3']['child2'].get("year"))

my_dict = {
    "color": "black",
    "salary": 10_000,
    "brand": "Volvo"
}

if my_dict.get("cica") or my_dict['color'] == "black":
    print("Valami")

my_dict = {
    "monthly_fee": 0
}

if my_dict.get("monthly_fee"):
    if my_dict['monthly_fee'] == 0:
        my_dict['monthly_fee'] = 4000

if 0:
    print("valami")
print(my_dict)