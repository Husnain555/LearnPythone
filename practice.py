fruits = []
f1 = input("Enter a fruit name:")
fruits.append(f1)
print(fruits)

marks = []
student1 = input("Enter a student score:")
marks.append(student1)
student2 = input("Enter a student score:")
marks.append(student2)
marks.sort()
print(marks)
# its sort but our marks was in a string form so its sorted like string but if we need to fully sort students we need to convert it in the
# int type like
marks2 = []

student1 = int(input("Enter a student score:"))
marks2.append(student1)
student2 = int(input("Enter a student score:"))
marks2.append(student2)
marks2.sort()
print(marks2)


num = [10,23,24,3532,543,635]

print(sum(num))
print(min(num))
print(max(num))

print(len(num))
a = num.count(10)
print(a)