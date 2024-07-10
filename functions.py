# Crown Crafted Content

# Localization/scope
name = "Crown Crafted"
def setnameto(new_string):
    name = new_string
    print("Locally:", name)

setnameto("Bill")  # <-- doesn't affect global variable, only local
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


# FUNCTIONS AS VARIABLES/OBJECTS
print("hello Function is located at: " + str(hello))  # <-- DATA MEMORY POSITION
hi = hello
hi(first="Jack", last="Johnson", extra="The 3rd")  # can be used as a duplicate

say = print
say("\nPrinting without the print function!")

# HIGH ORDER FUNCTION
#   a function that either:
#       accepts a function as an argument
#       or returns a function (basically instantiating/objectifying)

# ACCEPTING FUNCTIONS v
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
# ACCEPTING FUNCTIONS ^

# RETURNING FUNCTIONS v
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

print(str(divisor(7)(2)))

half = divisor(2)
print(str(half(10)))
# RETURNING FUNCTIONS ^
