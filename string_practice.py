# enter the user name with like good morning ...
import datetime
date = datetime.date.today().strftime("%Y-%m-%d")


name = input("Please enter your name:")
greeting="Hello,%s!" %name
print(f"Good Morning {name}")
print(greeting)


letter = '''Dear <|NAME|>, you are selected for interview on this date <|DATE|>'''
name = input("Please enter your name:")
final_letter = letter.replace("<|NAME|>", name).replace("<|DATE|>", date)
print(final_letter)


# find double space between doubl strings

greet = "hello Husnin you are very good "
print(greet.find(" "))