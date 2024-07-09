import math
# CrownCraftedContent
# Math operations, string operations, string slicing

print("\n*This script is strictly for simple operations learning*")

print("\nMATH FUNCTIONS")
print("\tSingle Value Calculations")
value = 5.65
print("\t\tStarting value = " + str(value))
print("\t\tRounded = " + str(round(value)))  # 2nd parameter is # of indices behind decimal (default = 0)
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


# STRING SLICING
#       slicing = create a substring by extracting elements from another string
#       indexing[] or slice()

# Indexing
#       [start:stop:step]
print("\nSTRING INDEXING")
name = "Crown Crafted"
first_letter = name[0]  # start at 0
first_name = name[0:5]  # start at 0, end before 5 (ending non-inclusive)
# ^ also written as name[0:5:1] or name[:5]
print("\t\t" + first_name + " starts with " + first_letter)
last_name = name[6:]  # easier way to write ALL from index 6 until the END (aka name[6:len(name)])
print("\t\t" + "Last Name: " + last_name)
odd_characters = name[0:len(name):2]  # name[::2] for simplification
print("\t\tEvery odd character: " + odd_characters)
reversed_name = name[::-1]
print("\t\tReversed name: " + reversed_name)

# Slice Function
#       Involves creating a (reusable) slice object
print("\tSLICE FUNCTION")
website1 = "http://google.com"
website2 = "http://wikipedia.com"
tmp_slice = slice(7, -4)  # 2nd parameter is a negative index (simply works inversely)
print("\t\t" + website1[tmp_slice])  # 1st website
print("\t\t" + website2[tmp_slice])  # 2nd website

# Index Operator []
#       gives access to a sequence's elements
using_name = "crown Crafted!"
if using_name[0].islower():
    using_name = using_name.capitalize()

first = using_name[:5].upper()
last = using_name[6:].lower()
ending_char = using_name[-2]  # because ! is at -1
print(first, last, "ends with", ending_char)
