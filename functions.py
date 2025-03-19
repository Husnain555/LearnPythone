a = 12
b = 20
c = 30
def add(a,b,c):
    return a+b+c
def subtract(a,b,c):
    return a-b-c

print (add(a,b,c))
print (subtract(a,b,c))

# find the factorail of number
def factorail (n):
    if n == 1 or n == 0:
        return 1
    return n * factorail(n - 1)
n = int(input("Please enter a number to find its factorail: "))
print(factorail(n))