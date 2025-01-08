s1 = 'GeeksforGeeks'

# anonymous function
s2 = lambda func: func.upper()


people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

data = dict(sorted(people.items()))

print(people.items())

# lambda anonymous function
data = dict(sorted(people.items(), key=lambda item: item[1]))

print(data)

# filter, map, reduce, lambda -> ezek frequentált használata -> funkcionális programozás



# print(s2(s1))