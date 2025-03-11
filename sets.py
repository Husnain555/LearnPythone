# sets is a collection of well define objects
# to make an empty set we do
s = set()
print(s,type(s))

# we dont repeat element in sets
# like here
a = {1,10,2,3,4,4,5,7,7,87,6,5,5,4,4,"husnain"}
b = {10,11,12,13}
# print(a)
# print(type(a))
# a.add(566)
# print(a)

c = a.union(b)
print(c)
d = a.intersection(b)
print(d)
e = a.difference(b)
print(e)