# zip(*iterables) = aggregate elements from two or more iterables (lists, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element


usernames = ["Crown", "Crafted", "Content"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ("1/1/2021", "1/2/2021", "1/3/2021")

users = zip(usernames, passwords, login_date)

print(type(users))
print(str(users))
print()
for i in users:
    print(i)

#for key, value in users.items():
#    print(key + " : " + value)