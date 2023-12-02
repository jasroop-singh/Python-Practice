from main import Product

print("Program 1:")
print()

# initialize the object
apple = Product("Apple", 0.40, 3)

# print using the methods
print("Initial: ")
print("Code:", apple.get_code())
print("Price:", apple.get_price())
print("Count:", apple.get_count())
print()

# loop until user quits
while True:
    print("1. Add count to inventory")
    print("2. Subtract count from inventory")
    print("3. Quit")
    print()

    # ask user for the choice
    userInput = input("Please enter the number of choice: ")

    # logic and calling specific methods from Product class
    if userInput == "1":
        count = int(input("Enter the count: "))
        apple.add_inventory(count)
        print("New Count after adding", count, "Apples:", apple.get_count())
        print()
    elif userInput == "2":
        count = int(input("Enter the count: "))
        apple.sell_inventory(count)
        if count < apple.get_count():
            print("New Count after selling", count, "Apples:", apple.get_count())
            print()
    elif userInput == "3":
        print("Program Ending!")
        break
    else:
        print("Invalid choice!")
        print()

# hardcoded way
"""
Hardcoded!!
goldenApple = Product("Golden Apple", 0.55, 7)
print()
print("Code:", goldenApple.get_code())
print("Price:", goldenApple.get_price())
print("Count:", goldenApple.get_count())

goldenApple.add_inventory(2)

print()
print("New Count after adding 2 Golden Apples:", goldenApple.get_count())

goldenApple.sell_inventory(13)

print()
goldenApple.sell_inventory(3)
print("New Count after selling 3 Golden Apples:", goldenApple.get_count())
"""





