"""

"""

my_dict = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : [
         {
            "name" : "Emil",
            "year" : 2004
        }
    ],
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
    },
    "kulcs": print
}

print(my_dict["child2"][0])
print(len(my_dict['child2']))
print(my_dict['kulcs'])

my_dict['child1']['salary'] = 40_000
my_dict['child3']['child1']['salary'] = 40_000
my_dict['child2'][0]['salary'] = 40_000

print(my_dict.keys())
print(my_dict['child3']['child1'])
print(my_dict['child2'])
