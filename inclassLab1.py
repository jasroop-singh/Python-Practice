"""
Name: Jasroop Singh
Assignment: In-Class Lab 1
"""

# Program 1

number1 = int(input("Please enter 1st number: "))
number2 = int(input("Please enter 2nd number: "))
number3 = int(input("Please enter 3rd number: "))
number4 = int(input("Please enter 4th number: "))
print("")

if (number1 == number2 or number1 == number3 or number1 == number4) and (number2 == number3 or number2 == number4):
    print("Two Pairs!")
else:
    print("Not Two Pairs!")

print("")

# Program 2

string1 = input("Enter 1st String: ")
string2 = input("Enter 2nd String: ")
string3 = input("Enter 3rd String: ")
print("")

if string1 < string2 and string1 < string3:
    print(string1)
    if string2 < string3:
        print(string2)
        print(string3)
    else:
        print(string3)
        print(string2)
elif string2 < string1 and string2 < string3:
    print(string2)
    if string1 < string3:
        print(string1)
        print(string3)
    else:
        print(string3)
        print(string1)
elif string3 < string1 and string3 < string2:
    print(string3)
    if string2 < string1:
        print(string2)
        print(string1)
    else:
        print(string1)
        print(string2)
print("")
# Program 3

x = input("Please enter the name of month: ")
date = int(input("Please enter the date: "))
print("")

month = x.lower()

if date <= 0 or date > 31:
    print("Invalid!")
elif (month == "march" and date >= 20) or (month == "april" and date <= 30) or month == "may" or (
        month == "june" and date <= 20):
    print("The season is Spring!")
elif (month == "june" and (21 <= date <= 30)) or month == "july" or month == "august" or (
        month == "september" and date <= 21):
    print("The season is Summer!")
elif (month == "september" and (22 <= date <= 30)) or month == "october" or (month == "november" and date <= 30) or (
        month == "december" and date <= 20):
    print("The season is Autumn!")
elif (month == "december" and date >= 21) or month == "january" or (month == "february" and date <= 28) or (
        month == "march" and date <= 19):
    print("The season is Winter!")
else:
    print("Invalid!")
