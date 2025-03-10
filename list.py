friends = ["Husnain",5,5.03,"awais","zaman"]
print(friends)

print(friends[0])


friends[0] = "Bilal"
print(friends)


print(friends[2:4])


print(friends.reverse())
count = friends.count("Bilal")
print(count)

inserting = friends.insert(4,"Ali")
friends.pop(3)
print(friends)

friends.remove("Bilal")
print(friends)