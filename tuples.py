# a collection with immutable
# list ws a collection which mutable
# string was also  which in imutable

a = (1,)
print(type(a))   #its gives us a class tuple

# we cant change the tuple
b = (1,2,"husnain",00153565.4568,"Husnain2")
print(b)

no = b.count("husnain")
print(no)
concat = a + b
print(concat)

# it concat a with b