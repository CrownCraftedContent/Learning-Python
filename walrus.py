# walrus operator

#   new as of Python 3.8
#   assignment expression aka walrus operator (expression rather than equation)
#   assigns values to variables as part of a larger expression

# happy = True
# print(happy)

print(happy := True)

# ------------------------------------------------------

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == 'quit':
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != 'quit':
    foods.append(food)
print("You appear to enjoy " + str(foods))