marks = {
    "husnain":20,
    "awais":30,
    "zaman":40
}

print(marks, type(marks))
for item in marks.items():
    print(item)

print(marks.update({"husnain":30}))
print(marks)

print(marks["husnain"])
# it print the marks of the spesific keys if its avalible and if the key is worng then its gives us the error
# print(marks["husnain2"])

# to tackle this error we use .get method

print(marks.get("awais2"))