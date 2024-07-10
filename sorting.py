# sort() method     = used with lists
# sorted() function = used with iterables (which can include lists)

# LISTS
# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
# students.sort(reverse=True)  # optional keyword arguments key and/or reverse

# OTHER ITERABLES
students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
sorted_students = sorted(students, reverse=True)  # returns a list but accepts an iterable as an argument
# same optional keywords

students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

age = lambda ages:ages[2]  # def(ages) return ages[2]
students.sort(key=age)  # a method for lists specifically
#   a different form of iterable, such as a tuple,
#   would need to iterate using the sorted() function instead
for i in students:
    print(i)

