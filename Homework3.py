"""
Name: Jasroop Singh
Class: CS2520.01
Homework 3
"""

# Program 1

print("")
print("Program #1:")
print("")

# get user input
x = input("Please enter the Card Notation: ")

print("")

# check for the index positions and assign them
first = x[0]
second = x[1]

firstValue = ""
secondValue = ""

isTrue = True

# check if the length is 2 and assign the values
if len(x) == 2:
    if first == "A":
        firstValue = "Ace"
    elif first == "2":
        firstValue = "Two"
    elif first == "3":
        firstValue = "Three"
    elif first == "4":
        firstValue = "Four"
    elif first == "5":
        firstValue = "Five"
    elif first == "6":
        firstValue = "Six"
    elif first == "7":
        firstValue = "Seven"
    elif first == "8":
        firstValue = "Eight"
    elif first == "9":
        firstValue = "Nine"
    elif first == "J":
        firstValue = "Jack"
    elif first == "Q":
        firstValue = "Queen"
    elif first == "K":
        firstValue = "King"

# check if the length is 3 and the number is "10", assign the suit to the 2nd index
elif len(x) == 3:
    third = x[2]
    if (first == "1" and second == "0") and (third == "S" or third == "D" or third == "C" or third == "H"):
        firstValue = "Ten"
        if third == "H":
            secondValue = "Hearts"
        elif third == "S":
            secondValue = "Spades"
        elif third == "D":
            secondValue = "Diamonds"
        elif third == "C":
            secondValue = "Clubs"
        else:
            isTrue = False
    else:
        isTrue = False
else:
    isTrue = False

if second == "H":
    secondValue = "Hearts"
elif second == "S":
    secondValue = "Spades"
elif second == "D":
    secondValue = "Diamonds"
elif second == "C":
    secondValue = "Clubs"

# prints the answer if conditions are met, else print invalid
if isTrue:
    print(firstValue + " of " + secondValue)
else:
    print("Invalid")

# Program 2

print("")
print("Program #2:")
print("")

# get user input
unitFrom = input("Convert From (fl oz, gal, oz, lb, in, ft, mi): ")
unitTo = input("Convert To (ml, l, g, kg, mm, cm, m, km): ")
value = float(input("Please enter the Value: "))

print("")

# convert it to lowercase
unitFrom.lower()
unitTo.lower()

# calculations
flToMl = value * 29.5735
flToL = flToMl / 1000
flToG = flToMl
flToKg = flToL

galToMl = value * 3785.411784
galToL = galToMl / 1000
galToG = galToMl
galToKg = galToL

ozToMl = flToMl
ozToL = flToL
ozToG = value * 28.3495
ozToKg = ozToG / 1000

lbToMl = value * 453.6
lbToL = lbToMl / 1000
lbToG = value * 453.592
lbToKg = lbToG / 1000

inToMm = value * 25.4
inToCm = inToMm / 10
inToM = inToMm / 1000
inToKm = inToM / 1000

ftToMm = value * 304.8
ftToCm = ftToMm / 10
ftToM = ftToMm / 1000
ftToKm = ftToM / 1000

miToM = value * 1609.34
miToMm = miToM * 1000
miToCm = miToM * 100
miToKm = miToM / 1000

# use if and elif to determine what the user input for the conversions
if unitFrom == "fl oz" and unitTo == "ml":
    print(str(value) + " " + unitFrom + " = " + str(flToMl) + " " + unitTo)
elif unitFrom == "fl oz" and unitTo == "l":
    print(str(value) + " " + unitFrom + " = " + str(flToL) + " " + unitTo)
elif unitFrom == "fl oz" and unitTo == "g":
    print(str(value) + " " + unitFrom + " = " + str(flToG) + " " + unitTo)
elif unitFrom == "fl oz" and unitTo == "kg":
    print(str(value) + " " + unitFrom + " = " + str(flToKg) + " " + unitTo)
elif unitFrom == "gal" and unitTo == "ml":
    print(str(value) + " " + unitFrom + " = " + str(galToMl) + " " + unitTo)
elif unitFrom == "gal" and unitTo == "l":
    print(str(value) + " " + unitFrom + " = " + str(galToL) + " " + unitTo)
elif unitFrom == "gal" and unitTo == "g":
    print(str(value) + " " + unitFrom + " = " + str(galToG) + " " + unitTo)
elif unitFrom == "gal" and unitTo == "kg":
    print(str(value) + " " + unitFrom + " = " + str(galToKg) + " " + unitTo)
elif unitFrom == "oz" and unitTo == "ml":
    print(str(value) + " " + unitFrom + " = " + str(ozToMl) + " " + unitTo)
elif unitFrom == "oz" and unitTo == "L":
    print(str(value) + " " + unitFrom + " = " + str(ozToL) + " " + unitTo)
elif unitFrom == "oz" and unitTo == "g":
    print(str(value) + " " + unitFrom + " = " + str(ozToG) + " " + unitTo)
elif unitFrom == "oz" and unitTo == "kg":
    print(str(value) + " " + unitFrom + " = " + str(ozToKg) + " " + unitTo)
elif unitFrom == "lb" and unitTo == "ml":
    print(str(value) + " " + unitFrom + " = " + str(lbToMl) + " " + unitTo)
elif unitFrom == "lb" and unitTo == "l":
    print(str(value) + " " + unitFrom + " = " + str(lbToL) + " " + unitTo)
elif unitFrom == "lb" and unitTo == "g":
    print(str(value) + " " + unitFrom + " = " + str(lbToG) + " " + unitTo)
elif unitFrom == "lb" and unitTo == "kg":
    print(str(value) + " " + unitFrom + " = " + str(lbToKg) + " " + unitTo)
elif unitFrom == "in" and unitTo == "mm":
    print(str(value) + " " + unitFrom + " = " + str(inToMm) + " " + unitTo)
elif unitFrom == "in" and unitTo == "cm":
    print(str(value) + " " + unitFrom + " = " + str(inToCm) + " " + unitTo)
elif unitFrom == "in" and unitTo == "m":
    print(str(value) + " " + unitFrom + " = " + str(inToM) + " " + unitTo)
elif unitFrom == "in" and unitTo == "km":
    print(str(value) + " " + unitFrom + " = " + str(inToKm) + " " + unitTo)
elif unitFrom == "ft" and unitTo == "mm":
    print(str(value) + " " + unitFrom + " = " + str(ftToMm) + " " + unitTo)
elif unitFrom == "ft" and unitTo == "cm":
    print(str(value) + " " + unitFrom + " = " + str(ftToCm) + " " + unitTo)
elif unitFrom == "ft" and unitTo == "m":
    print(str(value) + " " + unitFrom + " = " + str(ftToM) + " " + unitTo)
elif unitFrom == "ft" and unitTo == "km":
    print(str(value) + " " + unitFrom + " = " + str(ftToKm) + " " + unitTo)
elif unitFrom == "mi" and unitTo == "mm":
    print(str(value) + " " + unitFrom + " = " + str(miToMm) + " " + unitTo)
elif unitFrom == "mi" and unitTo == "cm":
    print(str(value) + " " + unitFrom + " = " + str(miToCm) + " " + unitTo)
elif unitFrom == "mi" and unitTo == "m":
    print(str(value) + " " + unitFrom + " = " + str(miToM) + " " + unitTo)
elif unitFrom == "mi" and unitTo == "km":
    print(str(value) + " " + unitFrom + " = " + str(miToKm) + " " + unitTo)
else:
    print("Invalid Conversion!")

# Program 3

print("")
print("Program #3:")
print("")

# get user input
number = int(input("Enter an integer between 1 and 3999: "))

print("")

num = number
result = ""
# print("Hello" * 3)

# check if the number is between 1 - 3999
if number <= 1 or number > 3999:
    print("Invalid Input!")
else:
    # get the number of thousands
    if number >= 1000:
        mult = number // 1000
        # attaches "M" how much ever the thousand's number is
        result = result + "M" * mult
        # get remainder
        number = number % 1000

    # repeat same process like thousand's
    if number >= 100:
        mult = number // 100
        if mult == 9:
            result = result + "CM"
        elif mult == 8:
            result = result + "DCCC"
        elif mult == 7:
            result = result + "DCC"
        elif mult == 6:
            result = result + "DC"
        elif mult == 5:
            result = result + "D"
        elif mult == 4:
            result = result + "CD"
        else:
            result = result + "C" * mult
    number = number % 100

    if number >= 10:
        mult = number // 10
        if mult == 9:
            result = result + "XC"
        elif mult == 8:
            result = result + "LXXX"
        elif mult == 7:
            result = result + "LXX"
        elif mult == 6:
            result = result + "LC"
        elif mult == 5:
            result = result + "L"
        elif mult == 4:
            result = result + "XL"
        else:
            result = result + "X" * mult
    number = number % 10

    if number >= 0:
        if number == 9:
            result = result + "IX"
        elif number == 8:
            result = result + "VIII"
        elif number == 7:
            result = result + "VII"
        elif number == 6:
            result = result + "VI"
        elif number == 5:
            result = result + "V"
        elif number == 4:
            result = result + "IV"
        elif number == 3:
            result = result + "III"
        elif number == 2:
            result = result + "II"
        elif number == 1:
            result = result + "I"

    # print the roman numeral
    print(str(num) + " in Roman Numeral is: " + result)