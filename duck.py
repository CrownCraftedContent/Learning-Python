# CrownCraftedContent

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")
class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)  # duck is a required parameter

person.catch(chicken)  # <-- chicken has all methods necessary to fit the needs of this call
#   if chicken didn't have the necessary contents, an error would be thrown:
#   Attribute Error: 'Chicken' object has no attribute 'walk' (walk or whatever attribute is missing)
