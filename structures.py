# CrownCraftedContent
# Lists, Tuples, Etc.

# LISTS
print("LISTS")
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]  # set list
food[0] = "sushi"  # adjust an element

food.append("ice cream")
food.remove("hotdog")
food.pop()  # removes the last element
food.insert(0, "cake")  # adds to a certain index
food.sort()
food.clear()

# TUPLES
print("TUPLES")
#   a Tuple is a collection which is ordered and unchangeable
#   is used to group together related data
student = ("Crown", 21, "male")
print("\tOccurrences" + str(student.count("Crown")))