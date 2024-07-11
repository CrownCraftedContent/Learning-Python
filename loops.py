import timing
# CrownCraftedContent
# while loops, for loops, nested loops, time module

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
    date = input("Enter the date: ")  # empty strings are not stored (considered non-truthy)

while True:
    title = input("What should I call you?: ")
    if title != "":
        break

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
print("\tFinal number in range(1, 5) is " + str(final_number))  # 4

every_other_number = "\tEvery other number:"
for i in range(50, 100, 2):
    every_other_number = every_other_number + " " + str(i)
print(every_other_number)

print("\tWord")
for i in "Word":
    print("\t\t" + str(i))

input("Hit ENTER to start Timer")
print("\t10 Seconds added to the clock")
for seconds in range(10,0,-1):
    print("\t\t" + str(seconds))
    time.sleep(1)
print("\tTimer has ended.")

# NESTED LOOPS
#       The inner loop will finish all of its iterations before the outer loop continues its iteration
rows = round(float(input("How many rows?: ")))
columns = round(float(input("How many columns?: ")))
symbol = input("Enter a symbol to use: ")

print("Printing grid")
for i in range(rows):
    for v in range(0, columns):  # or range(1, columns+1)
        print(symbol, end="")  # instead of the traditional , end="\n"      [ALTERNATIVE PRINT ENDING]
    print()
print("Done")
