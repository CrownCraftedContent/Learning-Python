#   Abstract classes prevent a user from creating an object of that class
#   compels a user to override abstract methods in a child class

#   abstract class = a class which contains one or more abstract methods
#   abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod
# from abstract-based-class

class Vehicle(ABC):  # abstract-based-class
    @abstractmethod
    def go(self):  # abstract method
        pass

    def stop(self):  # regular method
        print("This vehicle has stopped")

class Car(Vehicle):
    def go(self):
        print("You ride the car")
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

# vehicle = Vehicle()  # can be created only if NO abstract METHODS are present (1 or more abs. methods)
car = Car()  # go() must be overridden by the child for this to be created
moto = Motorcycle()  # go() must be overridden by the child for this to be created
car.go()
moto.stop()
car.stop()
