class Circle:
    pi = 3.14159  # Class variable which are bound with class
    
    def __init__(self, radius):
        self.radius = radius # Instance Variable in python which are bound with object
    
    def area(self):
        return self.pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

# Creating a Circle instance and calculating its area
circle1 = Circle(5)
print("Circle 1 Area:", circle1.area())

# Using a class method to create a Circle instance from diameter
circle2 = Circle.from_diameter(10)
print("Circle 2 Area:", circle2.area())


# In this example, we have a Circle class with an instance method area that calculates 
# the area of the circle. We also have a class method from_diameter that creates a Circle 
# instance based on the diameter and returns it.

# The @classmethod decorator marks the from_diameter method as a class method.
# The parameter cls is used inside the from_diameter method to refer to the class itself.
# By using cls, we can create and return a new instance of the Circle class using the class constructor.
# You can use class methods to create alternative constructors, perform class-level operations, 
# or provide utility functions related to the class.

# Remember, the key distinction is that instance methods (with self as the first parameter) operate 
# on instances of the class, while class methods (with cls as the first parameter) operate on the class itself.