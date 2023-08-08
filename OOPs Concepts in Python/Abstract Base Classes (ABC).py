# Abstract Base Classes (ABCs):

# Abstract Base Classes define a common interface for its subclasses. 
# They provide a way to define a set of methods that must be implemented by concrete subclasses.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

circle = Circle(5)
print(f"Circle Area: {circle.area()}")





# Assignment:
# Create a hierarchy of vehicle classes, including a base class Vehicle and subclasses Car, Bicycle, 
# and Motorcycle. Implement methods and attributes that are relevant to each type of vehicle. 
# Use method overriding and super() to customize and extend methods as needed.
        
        
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Bicycle Type: {self.type}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_displacement):
        super().__init__(make, model, year)
        self.engine_displacement = engine_displacement

    def display_info(self):
        super().display_info()
        print(f"Engine Displacement: {self.engine_displacement}")

# Creating instances of the classes
car = Car("Toyota", "Camry", 2022, 4)
bicycle = Bicycle("Trek", "Mountain Bike", 2022, "Mountain")
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, "1200cc")

# Displaying vehicle information
car.display_info()
print()
bicycle.display_info()
print()
motorcycle.display_info()
