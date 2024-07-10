# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (can be thought of like a shortcut)
#                   (useful if needed for a short period of time, temporary/throw-away)

# lambda parameters:expression
# def double(x):
#    return x * 2
# VVV
double = lambda x: x * 2
print(double(5))
multiply = lambda x, y: x * y
print(multiply(5, 6))
add = lambda x, y, z: x + y + z
print(add(5,6,7))
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("John", "Doe"))
age_check = lambda age: True if age >= 18 else False  # aka lambda age: age >= 18
print(age_check(18))
