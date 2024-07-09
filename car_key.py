from car_class import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")  # doesn't need self arg
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.drive()
car_2.stop()

# car_1.wheels = 2
Car.wheels = 2  # <-- affects value for all instances created
print(car_1.wheels, car_2.wheels)

print(Car.wheels)  # <-- works for class variables
