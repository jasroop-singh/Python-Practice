"""
Name: Jasroop Singh
Class: CS2520.01
Assignment: In-Class Lab 4
"""
import random

# Program 1: Palindrome

print("Program 1:")
def isPalindrome(string, start, end):
    if len(string) == 1:
        return True
    if start >= end:
        return True
    if string[start] == string[end]:
        return isPalindrome(string, start + 1, end - 1)
    else:
        return False


userInput = input("Please enter a string: ")
j = len(userInput) - 1
result = isPalindrome(userInput, 0, j)
if result == True:
    print("It is a palindrome!")
elif result == False:
    print("It is not a palindrome!")
print()


# Program 2:
print("Program 2:")
def an(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        half = n // 2
        return an(a, half) ** 2
    else:
        return an(a, n - 1) * a


aInput = int(input("Please enter the value of \'a\': "))
nInput = int(input("Please enter the value of \'n\': "))
result = an(aInput, nInput)
print(result)
print()

# Program 3:


# Program 4:
print("Program 4:")
def draw_triangle(base):
    if base < 1:
        return
    else:
        draw_triangle(base - 2)
        spaces = (triangleLength - base) // 2
        print(" " * spaces + "*" * base)


triangleLength = int(input("Please input the length: "))
draw_triangle(triangleLength)
print()

# Program 5:
print("Program 5:")
def calc_toll(hour, morning, weekend):
    if weekend == "true" and morning == "true":
        if 1 <= hour <= 6 or hour == 12:
            return 1.05
        elif 7 <= hour <= 11:
            return 2.15
    elif weekend == "true" and morning == "false":
        if 1 <= hour <= 7 or hour == 12:
            return 2.15
        elif 8 <= hour < 12:
            return 1.10
    elif weekend == "false" and morning == "true":
        if hour < 7 or hour == 12:
            return 1.15
        elif 7 <= hour <= 9:
            return 2.95
        elif 10 <= hour <= 11:
            return 1.90
    elif weekend == "false" and morning == "false":
        if hour == 12 or 1 <= hour <= 2:
            return 1.90
        elif 3 <= hour <= 7:
            return 3.95
        elif 8 <= hour <= 11:
            return 1.40


hourInput = int(input("Please enter the hour: "))
isMorning = (input("Please enter if the time is morning (True/False): ")).lower()
isWeekend = (input("Please enter if it is weekend (True/False): ")).lower()
result = calc_toll(hourInput, isMorning, isWeekend)
print("Your fees is: $" + str(result))
print()

# Program 6:
print("Program 6:")
def coin_flip(num):
    if num == 0:
        return
    else:
        coin_flip(num - 1)
        x = random.randint(0, 1)
        if x == 0:
            print("Tails")
        elif x == 1:
            print("Heads")


coinTimes = int(input("Enter a number: "))
coin_flip(coinTimes)

