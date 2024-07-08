import math

print("\n*This script is strictly for simple operations learning*")

print("\nMATH FUNCTIONS")
print("\tSingle Value Calculations")
value = 5.65
print("\t\tStarting value = " + str(value))
print("\t\tRounded = " + str(round(value)))
print("\t\tCeiling = " + str(math.ceil(value)))
print("\t\tFloored = " + str(math.floor(value)))
print("\t\tSquare root = " + str(math.sqrt(value)))

print("\n\tMultiple Value Calculations")
x, y, z, = 1, 2, 3
print("\t\tMax out of set = " + str(max(x,y,z)))
print("\t\tMin out of set = " + str(min(x,y,z)))


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
