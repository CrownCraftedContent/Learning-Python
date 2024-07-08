# CrownCraftedContent

# Sidenote: refrain from creating infinite loops

# WHILE LOOPS
#       iterate an unlimited number of times (by default)
print("WHILE LOOPS")
name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

date = None
while not date:
    date = input("Enter the date: ")

print("According to you, the date is " + date)


# FOR LOOPS
#       iterate a limited number of times (always, unlike WHILE loops)
#       range()'s 2nd parameter is exclusive, much like with slicing strings
print("FOR LOOPS")
print_string1 = "\tLoop 1:"
for i in range(10):  # 1 to end point
    print_string1 = print_string1 + " " + str(i)
print(print_string1)

print_string2 = "\tLoop 2:"
for i in range(50, 100):  # start to end point
    print_string2 = print_string2 + " " + str(i)
print(print_string2)

final_number = None
for i in range(1, 5):
    final_number = i
print("\tFinal number in range is " + str(final_number))  # 4
