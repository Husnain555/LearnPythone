marks = [int(input(f"Please Enter Your maks of {i+1} Subject")) for i in range(4)]
total = sum(marks)
total_percentage = (total / (4 * 100)) * 100
print(total_percentage)
if total_percentage >= 90:
    print("You Grade is A")
elif total_percentage >= 80:
    print("You Grade is B")
elif total_percentage >= 70:
    print("You Grade is C")
elif total_percentage >= 60:
    print("You Grade is D")
else:print("You Grade is F")