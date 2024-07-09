# Crown Crafted Content

# Localization/scope
name = "Crown Crafted"
def setnameto(new_string):
    name = new_string
    print("Locally:", name)

setnameto("Bill")
print("Afterword, Globally:", name)

# *args
#       a parameter which will pack all arguments into a tuple
#       useful so that an argument can accept a varying amount of arguments
#       common convention is to just name it args
def add(*stuff):  # or *args
    total = 0
    stuff = list(stuff)  # tuple to list
    stuff.append(4)
    if len(stuff) >= 3:
        stuff[2] = 0
    for i in stuff:
        total += i
    return total

print(add(1,2,3))

# **kwargs
#       parameter that will unpack all arguments into a dictionary
#       useful so that a function can accept a varying amount of keyword arguments
#       kwargs is common naming convention but ** is important piece

def hello(**kwargs):
    #  print("Hello", kwargs.get('first'), kwargs.get('last'))
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(first="Jack", last="Johnson", extra="The 3rd")

