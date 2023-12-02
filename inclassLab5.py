"""
Name: Jasroop Singh
Assignment: In class lab 5
Class: CS2520
"""

import random

# Program 1:

# main program that runs until user quits
print("Program 1:")
def mainProgram1():
    run = True
    while run:
        # initial list being used
        list1 = [72, 34, 51, 19, 88, 6, 43, 93, 59, 12, 34]
        
        # print the menu
        print("Menu:")
        print("a. Swap the first and last elements in the list.")
        print("b. Shift all elements by one to the right and move the last element into the first position.")
        print("c. Replace all even elements with 0.")
        print("d. Replace each element except the first and last by the larger of its two neighbors.")
        print("e. Remove the middle element if the list length is odd, or the middle two elements if the length is "
              "even.")
        print("f. Move all even elements to the front.")
        print("g. Return the second-largest element in the list.")
        print("h. Return true if the list is currently sorted in increasing order.")
        print("i. Return true if the list contains two adjacent duplicate elements.")
        print("j. Return true if the list contains duplicate elements")
        print("q. Type Q to exit the program.")
        print()
        userIn = input("Please enter the character: ").upper()
        
        # check which character did user input and perform designated functions
        if userIn == "A":
            swap(list1, 0, -1)
            print()
        elif userIn == "B":
            shift(list1)
            print()
        elif userIn == "C":
            replace0(list1)
            print()
        elif userIn == "D":
            replaceMid(list1)
            print()
        elif userIn == "E":
            removeMiddle(list1)
            print()
        elif userIn == "F":
            evenFront(list1)
            print()
        elif userIn == "G":
            secondLargest(list1)
            print()
        elif userIn == "H":
            result = increasing(list1)
            print("Answer is:", result)
            print()
        elif userIn == "I":
            result = hasAdjacentDuplicates(list1)
            print("Answer is:", result)
            print()
        elif userIn == "J":
            result = hasDuplicates(list1)
            print("Answer is:", result)
            print()
        elif userIn == "Q":
            run = False
        else:
            print("Invalid Character!")

# swaps the first and last element
def swap(myList, pos1, pos2):
    myList[pos1], myList[pos2] = myList[pos2], myList[pos1]
    print("Swap =", myList)

# shifts the last element to front
def shift(mylist):
    if len(mylist) >= 2:
        last_element = mylist.pop()
        mylist.insert(0, last_element)
        print("Answer = ", mylist)

# replaces ever even number with 0
def replace0(mylist):
    for i in range(len(mylist)):
        if mylist[i] % 2 == 0:
            mylist[i] = 0
    print(mylist)

# replace all the middle numbers with neighboring max
def replaceMid(mylist):
    if len(mylist) >= 3:
        for i in range(1, len(mylist) - 1):
            max_neighbor = max(mylist[i - 1], mylist[i + 1])
            mylist[i] = max_neighbor
    print(mylist)

# removes the middle numbers
def removeMiddle(mylist):
    length = len(mylist)
    if length % 2 == 1:
        middle_index = length // 2
        mylist.pop(middle_index)
    elif length % 2 == 0:
        middle_index = length // 2
        mylist.remove(middle_index)
        mylist.remove(middle_index + 1)
    print(mylist)

# shifts all the even number in front
def evenFront(mylist):
    evenElements = []
    oddElements = []

    for value in mylist:
        if value % 2 == 0:
            evenElements.append(value)
        else:
            oddElements.append(value)

    print(evenElements + oddElements)

# finds the second largest number present in the list
def secondLargest(mylist):
    largest = max(mylist)
    second = 0
    boolean = True
    for i in range(len(mylist)):
        if boolean:
            if mylist[i] < largest:
                second = mylist[i]
                boolean = False

        if mylist[i] > second and mylist[i] != largest:
            second = mylist[i]

    print(second)

# checks if the list is already sorted
def increasing(mylist):
    ascending = sorted(mylist)
    if mylist == ascending:
        return True
    else:
        return False

# checks if the list has any adjacent duplicates
def hasAdjacentDuplicates(mylist):
    for i in range(len(mylist) - 1):
        if mylist[i] == mylist[i + 1]:
            return True
    return False

# checks if the list has any duplicates
def hasDuplicates(mylist):
    n = len(mylist)
    for i in range(n):
        for j in range(i + 1, n):
            if mylist[i] == mylist[j]:
                return True
    return False


mainProgram1()

# Program 2
print()
print("Program 2: ")
# create initial empty array
diceList = []

# fill the array with random inputs from 1-6
for i in range(20):
    diceList.append((random.randint(1, 6)))

# initialize variables
startIndex = 0
currentLength = 1
currentStartIndex = 0
length = 0

# initialize current length from first element
for i in range(1, len(diceList)):
    if diceList[i - 1] == diceList[i]:
        currentLength += 1
    else:
        if length < currentLength:
            startIndex = currentStartIndex
            length = currentLength
        currentStartIndex = i
        currentLength = 1

# checks longest run
if currentLength > length:
    startIndex = currentStartIndex
    length = currentLength

# prints the values including the longest run
print("Dice rolls = ", end="")
for i in range(len(diceList)):
    if i == startIndex:
        print("(", end=" ")
    print(diceList[i], end=" ")
    if i == startIndex + length - 1:
        print(")", end=" ")


# Program 3:
print()
print()
print("Program 3: ")
# create initial list
myList = []

# fill the list with numbers from 1-10
for i in range(1,11):
    myList.append(i)

# create another list to hold the permutations
initial = []

# perform the permutations and print the list 10 times
for i in range(10):
    secondList = list(myList)
    permutation = []

    for j in range(10):
        # get the random position in the list
        randPos = random.randint(0, len(secondList) - 1)

        # pop that element
        remNum = secondList.pop(randPos)

        # append it into the new list
        permutation.append(remNum)

    # append to the main list
    initial.append(permutation)

    # Print the current permutation
    print(permutation)


