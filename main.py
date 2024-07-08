# CrownCraftedContent
# Printing, Variable Assignment, Casting, Input, If Statements, Exceptions

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


# USER INPUT
print("\nUSER INPUT")
clientName = input("\tWhat is your name?: ")
print("\tOkay, nice to meet you " + clientName)


# EXCEPTION HANDLING (lightly touched)
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

