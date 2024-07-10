# map() =      applies a function to each item in an iterable (list, tuple, etc.)
print("\nmap()")
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
from_euros = lambda data: (data[0], data[1] / 0.82)
print("Converting prices to Euros")
store_euros = list(map(to_euros, store))  # to_euros's data parameter takes each iterable item as an argument
for i in store_euros:
    print(str(i))
print("And now to dollars instead")
store_dollars = list(map(from_euros, store))
for i in store_dollars:
    print(str(i))
print("Original store should be unaltered:")
for i in store:
    print(str(i))

# -----------------------------------------------------------------------------------------------------
# filter() = creates a collection of elements from an iterable for which a function returns true
print("\nfilter()")
# filter(function, iterable)

friends = [("Rachel", 22),
           ("Monica", 21),
           ("Phoebe", 20),
           ("Joey", 19),
           ("Chandler", 24),
           ("Ross", 23)]

of_age = lambda data: data[1] >= 21
those_of_age = list(filter(of_age, friends))
for i in those_of_age:
    print(i)

# -----------------------------------------------------------------------------------------------------
# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs function on first two elements and repeats process until 1 value remains
print("\nfunctools.reduce()")
# functools.reduce(function, iterable)
import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y: x+y, letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y: x * y, factorial)
print("5! =", result)
