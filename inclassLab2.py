# Program 1

# get string from user
string = input("Please enter a string: ")
decrease = 0

# for loop to go through all the characters
for ch in string:

    #if character is equal to . or , or space then count them
    if ch == " " or ch == "." or ch == "," or ch == "!":
        decrease += 1

# print the total number minus all those special characters
print(len(string) - decrease)
print("")

# Program 2

# get string from user
string2 = input("Please enter the Password: ")

# for loop to go through all the characters
for ch in string2:

    # replace all the given characters
    if ch == "i":
        print(1, end="")
    elif ch == "a":
        print("@", end="")
    elif ch == "m":
        print("M", end="")
    elif ch == "B":
        print(8, end="")
    elif ch == "s":
        print("$", end="")
    else:
        print(ch, end="")
