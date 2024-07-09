class Car:
    wheels = 4  # class variable, stays default until changed
    def __init__(self, make, model, year, color):
        self.make = make  # instantiable (instance variable)
        self.model = model  # instantiable (instance variable)
        self.year = year  # instantiable (instance variable)
        self.color = color  # instantiable (instance variable)

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")
