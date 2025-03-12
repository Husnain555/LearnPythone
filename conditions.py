from typing import final


a = int(input("Please enter your age:"))
if a >= 18:
    print("You are young.")
elif a < 0 :
        print("You are  entering an invalid age .")
else:
    print("You are older.")

# find the greetest number thet user give in in put

numbers = [int(input(f"please enter the the number{i+1}: ")) for i in range(4)]
greatest = max(numbers)
if numbers.count(greatest) == len(numbers):
    print("All number are equal")
else:print("The greatest number is",greatest)