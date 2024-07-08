# CrownCraftedContent
# Lists, Tuples, Etc.

# LISTS
print("\nLISTS")
#   arrays (adjustable storage containers)
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
#   a Tuple is a collection which is ordered and unchangeable
#   is used to group together related data
student = ("Crown", 21, "male")
print(student.count("Crown"))  # print("\tOccurrences" + str(student.count("Crown")))
print(student.index("male"))
for x in student:
    print(x, end=" ")
if "Crown" in student:
    print("Crown is here!")

# SETS
print("\nSETS")
#   a collection which is unordered, unindexed, and does not retain duplicate values
#   faster than a list in search time
utensils = {"fork", "spoon", "knife", "knife"}  # doesn't keep extra knife
print("Size of utensils set = " + str(len(utensils)))
utensils.add("napkin")
utensils.remove("fork")
print("Utensils = " + str(utensils))
utensils.clear()
print("Utensils = " + str(utensils))  # prints set() which is the constructor of its class
dishes = {"bowl", "plate", "cup"}
# add one set to another using the update method
utensils.update(dishes)
print("Utensils = " + str(utensils))
