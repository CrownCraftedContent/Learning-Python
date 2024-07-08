# CrownCraftedContent

# Sidenote: refrain from creating infinite loops

# WHILE LOOPS
print("WHILE LOOPS")
name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

date = None
while not date:
    date = input("Enter the date: ")

print("According to you, the date is " + date)
