# Python Name Syntax = '_' for spaces
print("\nVARIABLE TYPES (+ Casting & Formatting)")
first_name = "First"
last_name = "Last"
full_name = first_name + " " + last_name  # concatenation
print(f"\tfull_name has a value of {full_name}\n\t\t and is a {type(full_name)}")  # formatting

age = 21
age += 1  # incrementing (NOTE: double space for in-line comments)
print("\tAge has a value of " + str(age) + f"\n\t\tand is a {type(age)}")  # casting

height = 250.5
print(f"\tHeight has a value of {height}\n\t\tand is a {type(height)}")  # formatting

whether_or_not = True
print("\twhether_or_not has a value of " + str(whether_or_not) + f"\n\t\tand is a {type(whether_or_not)}")  # casting


# Multiple assignment
print("\nMULTIPLE ASSIGNMENT")
guy_name, guy_age, guy_height = "Alex", 25, 275.4
print(f"\tThis guy {guy_name} is {guy_age} years old and {guy_height} cm tall.")
guy1 = guy2 = guy3 = guy4 = 30
print(f"\tThe ages are {guy1}, {guy2}, {guy3}, and {guy4}")


# STRING FUNCTIONS
print("\nSTRING FUNCTIONS")
test_string = "Find ABC not d"
print("\tThe length of the string is " + str(len(test_string)))
print("\tThe letter 'd' was found at position " + str(test_string.find("d")) + " in ''" + test_string + "''")  # find
print("\tCapitalization: " + test_string.capitalize())
print("\tUppercase: " + test_string.upper())
print("\tLowercase: " + test_string.lower())
print("\tIs our string a digit? " + str(test_string.isdigit()))
print("\tIs our string alphabetical? " + str(test_string.isalpha()))  # cannot contain spaces/numbers/etc.
print("\tHow many d's? " + str(test_string.count("d")))  # capitalization matters
print("\tReplacing spaces with hyphens: " + test_string.replace(" ", "-"))
print("\t3 times: " + test_string*3)


# USER INPUT
print("\nUSER INPUT")
clientName = input("\tWhat is your name?: ")
print("\tOkay, nice to meet you " + clientName)

clientInt = None
try:
    clientInt = int(input("\tEnter a float: "))
except ValueError as e:
    print(f"\t\tValue error: {e}")  # e cannot be cast into a string (or anything else)


# IF STATEMENTS
print("\nIF STATEMENTS")
if clientInt is None:
    print("\tUnable to repeat integer, none recorded.")
elif clientInt < 0:
    print("\tWe received a negative integer, " + str(clientInt) + ".")
else:
    print("\tWe received a positive integer, " + str(clientInt) + ".")

