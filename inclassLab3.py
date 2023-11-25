"""
Name: Jasroop Singh
Class: CS2520.01
Assignment: In Class Lab 3
"""

"""

# Program 1: (Doesnt work) 

def scramble(word):
    scrambledWords = ""

    if len(word) < 4:
        return word

    for x in word:
        if x == " ":
            temp = word[x - 2]
            word[x - 2] = word[x - 3]
            word[x - 3] = temp
            scrambledWords += word

    return scrambledWords


inputString = input("Please enter a sentence: ")

print(scramble(inputString))
"""

# Program 2
def main2():
    print("Program 2: ")
    print("")
    hrs = int(input("Please enter the hours: "))
    mins = int(input("Please enter the number of minutes: "))
    if hrs <= 0 or hrs >= 13 or mins < 0 or mins >= 60:
        print("Atleast 1 input is invalid!")
    else:
        print(getTimeName(hrs, mins))


def getTimeName(hrs, mins):
    name = ""

    if mins == 0:
        name = hourName(hrs) + " o\' clock"
    elif mins < 10:
        minsName = hourName(mins)
        name = minsName + " minutes past " + hourName(hrs)
    elif mins < 20:
        minsName = teenName(mins)
        name = minsName + " minutes past " + hourName(hrs)
    elif mins < 60:
        if mins == 30:
            name = "Half past " + hourName(hrs)
        elif mins == 45:
            name = "A quarter to " + hourName(hrs + 1)
        else:
            part = mins % 10
            minsName = tensName(mins) + " " + hourName(part)
            name = minsName + " minutes past " + hourName(hrs)

    return name


def hourName(hours):
    if hours == 1: return "One"
    if hours == 2: return "Two"
    if hours == 3: return "Three"
    if hours == 4: return "Four"
    if hours == 5: return "Five"
    if hours == 6: return "Six"
    if hours == 7: return "Seven"
    if hours == 8: return "Eight"
    if hours == 9: return "Nine"
    if hours == 10: return "Ten"
    if hours == 11: return "Eleven"
    if hours == 12: return "Twelve"
    return ""


def teenName(number):
    if number == 10: return "Ten"
    if number == 11: return "Eleven"
    if number == 12: return "Twelve"
    if number == 13: return "Thirteen"
    if number == 14: return "Fourteen"
    if number == 15: return "Fifteen"
    if number == 16: return "Sixteen"
    if number == 17: return "Seventeen"
    if number == 18: return "Eighteen"
    if number == 19: return "Nineteen"
    return ""


def tensName(number):
    if number >= 50: return "Fifty"
    if number >= 40: return "Forty"
    if number >= 30: return "Thirty"
    if number >= 20: return "Twenty"
    return ""




# Program 3

def menu():
    print("Program 3: ")
    start = 1
    while start == 1:
        print("")
        print("Today\'s menu is: ")
        print("1) Chicken")
        print("2) Steak")
        print("3) Quit")

        choice = int(input("Please enter the choice: "))

        if choice == 1:
            print("Order: Chicken")
        elif choice == 2:
            print("Order: Steak")
        elif choice == 3:
            print("Goodbye!!!")
            break
        else:
            print("Invalid Choice!")


menu()
