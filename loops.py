# for i in range(1,10):
#     print(i)

# i = 0
# while i < 11:
#     print(f"{i}Husnain")
#     i += 1

# my_list = [1, "hello", 3.14, True, [2, 4, 6], {"name": "Husnain"}]
# i = 0
# while i < len(my_list):
#      print(my_list[i])
#      i = i + 1
#
#
# name = "Husnain"
# for letter in name:
#     print(letter)


# print table of the input number
n = int(input("please enter a number: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")
# i = 1
# while i<= 10:
#     print(f"{n} x {i} = {n*i}")
#     i += 1

for i in range(2,n):
    if (n%i) == 0:
        print("The number is not a Prima Number")
        break
    else: print("The number is a Prima Number")



# names = ["Sara", "Sami", "Husnain", "Aliza", "Ahmed", "Fatima"]
# for name in names:
#     if name.startswith("S"):
#         print(f"greeting: {name}")
