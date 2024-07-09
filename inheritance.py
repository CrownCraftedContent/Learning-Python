# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:  # multi-level inheritance parent
    alive = True

class Animal(Organism):  # parent / class to be inherited

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):  # Rabit = child, Animal = parent class
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()

# -------------------------------------------------------------------------------------
# multiple inheritance = whn a child class is derived from more than one parent class
#   predefined class structures don't appear to be able to touch

class Prey:
    def flee(self):
        print("This animal flees")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):  # <-- multiple inheritance
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()