import random

x = random.randint(1,6)  # inclusive
y = random.random()
print(x, "and", y)

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
