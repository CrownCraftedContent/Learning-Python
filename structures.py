# CrownCraftedContent
# Lists, Tuples, Etc.

# LISTS
print("\nLISTS")
#       arrays (adjustable storage containers)
#       Functions: append, remove, pop, insert, sort, clear
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]  # set list
food[0] = "sushi"  # adjust an element
print(food)
food.append("ice cream")
food.remove("hotdog")
food.pop()  # removes the last element
food.insert(0, "cake")  # adds to a certain index
food.sort()
food.clear()

# TUPLES
print("\nTUPLES")
#       a Tuple is a collection which is ordered and unchangeable
#       is used to group together related data
#       Functions: count, index
student = ("Crown", 21, "male")
print(student.count("Crown"))  # print("\tOccurrences" + str(student.count("Crown")))
print(student.index("male"))
for x in student:
    print(x, end=" ")
if "Crown" in student:
    print("Crown is here!")

# SETS
print("\nSETS")
#       a collection which is unordered, unindexed, and does not retain duplicate values
#       faster than a list in search time
#       Functions: add, remove, clear, update, union, difference, intersection
utensils = {"fork", "spoon", "knife", "knife"}  # doesn't keep extra knife
print("Size of utensils set = " + str(len(utensils)))
for x in utensils:  # won't always be the same order
    print(x)
# add() utensils.add("napkin")
# remove() utensils.remove("fork")
# clear() utensils.clear()
# dishes = {"bowl", "plate", "cup", "knife"}
# update() utensils.update(dishes)  # add one set to another using the update method
# union() dinner_table = utensils.union(dishes)
# difference() print(utensils.difference(dishes))  # what utensils have that dishes doesn't (1st does that 2nd doesn't)
# intersection() print(utensils.intersection(dishes))

# DICTIONARIES
#       a changeable, unordered collection of unique keys with value pairs
#       fast because they use hashing, allow us to access a value quickly
capitals = {'USA': 'WASHINGTON DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# Errors can be caused by capitals['Germany']
print(capitals.get('Germany'))  # prints None
capitals.keys()
capitals.values()
capitals.items()
capitals.update({'Germany': 'Berlin'})  # can also update already existing keys
print(capitals.items())
capitals.pop('India')
capitals.clear()


print("\nLISTS CONTINUED (with comprehension)")
# list comprehension = a way to create a new list with less syntax
#       can mimic certain lambda functions, easier to read
#       list = [expression for item in iterable]
#       list = [expression for item in iterable if conditional]
#       list = [expression if/else for item in iterable]

squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1,11)]  # equivalent for loop above
print(squares)

students = [100,90,80,70,60,50,40,30,0]
# passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)

# dictionary comprehension = create dictionaries using an expression
#       can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: if/else for (key, value) in iterable}

cities_in_F = {'New York':25, 'Boston':75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# IF CONDITIONAL
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

# IF/ELSE
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: "WARM" if value >= 40 else "COLD" for (key, value) in cities.items()}
print(str(desc_cities))

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(str(desc_cities))
