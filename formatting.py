# Crown Crafted Content

# str.format()
#       optional method that gives users more control when displaying output

animal = "cow"
item = "moon"
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))  # positional argument
print("The {first} jumped over the {second}".format(first=animal, second=item))  # keyword arguments

text = "The {} jumped over the {}"
print(text.format(animal, item))


name = "Crown"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))  # adds padding 10 spaces
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # left aligned (default)
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # right aligned
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # center aligned
print("Hello, my name is {keyw:<10}. Nice to meet you".format(keyw=name))  # positional/keyword arguments go before colon

number = 3.14159
print("The number pi is {:.2f}".format(number))  # display two digits (rounds) after decimal (f = float)
number = 1000
print("The number is {:,}".format(number))  # adds a , to all triple digit locations
print("The number is {:b}".format(number))  # displays a binary representation of number
print("The number is {:o}".format(number))  # displays as an octal representation of the number
print("The number is {:X}".format(number))  # hexadecimal (x: for lowercase, X: for uppercase)
print("The number is {:E}".format(number))  # scientific notation (e: for lowercase, E: for uppercase)
