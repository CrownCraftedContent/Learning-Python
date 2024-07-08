# CrownCraftedContent
# Lists, Tuples, Etc.

# LISTS
print("\nLISTS")
#   arrays (adjustable storage containers)
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]  # set list
food[0] = "sushi"  # adjust an element

food.append("ice cream")
print(food)
print(food.__class__)

food.remove("hotdog")
food.pop()  # removes the last element
food.insert(0, "cake")  # adds to a certain index
food.sort()
food.clear()

# TUPLES
print("\nTUPLES")
#   a Tuple is a collection which is ordered and unchangeable
#   is used to group together related data
student = ("Crown", 21, "male")
print(student.count("Crown"))
# print("\tOccurrences" + str(student.count("Crown")))
print(student.index("male"))
