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
