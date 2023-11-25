"""
Name: Jasroop Singh
Class: CS2520.01
Assignment: Homework 2
"""

# Program 1

print("Program #1:")
print("")

# takes inputs from the user
first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
print("")

# perform arithmetic operations
add = first + second
print("Sum =", add)
difference = first - second
print("Difference =", difference)
product = first * second
print("Product =", product)
average = (first + second) / 2
print("Average =", average)
distance = abs(difference)
print("Distance =", distance)
maximum = max(first, second)
print("Maximum =", maximum)
minimum = min(first, second)
print("Minimum =", minimum)
print("")
print("")

# Program 2

print("Program #2:")
print("")

# takes inputs from the user
newCost = float(input("Enter cost of new car: "))
miles = float(input("Enter estimated miles driven per year: "))
gasPrice = float(input("Enter estimated gas price: "))
efficiency = float(input("Enter efficiency in miles per gallon: "))
resaleValue = float(input("Enter estimated resale value after 5 years: "))
print("")

# formula to calculate
totalCost = newCost + ((miles * gasPrice * 5) / efficiency) - resaleValue
print("Total Cost =", totalCost)
print("")
print("")

# Program 3

print("Program 3:")
print("")

# gets user inputs
firstTime = int(input("Please input the first time: "))
secondTime = int(input("Please input the second time: "))
print("")

# converts the numbers into hours and minutes
firstHour = firstTime // 100
firstMinute = firstTime % 100
secondHour = secondTime // 100
secondMinute = secondTime % 100

# converts hours into minutes
totalFirst = (firstHour * 60) + firstMinute
totalSecond = (secondHour * 60) + secondMinute

# get the difference
totalDifference = abs(totalFirst - totalSecond)

# converts the number back to hours and minutes
hours = totalDifference // 60
minutes = totalDifference % 60

# prints the output
print("Difference is:", hours, "Hours and", minutes, "Minutes")








