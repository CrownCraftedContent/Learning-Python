# map() =      applies a function to each item in an iterable (list, tuple, etc.)

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
