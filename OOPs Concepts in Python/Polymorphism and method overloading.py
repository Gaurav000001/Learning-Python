# Polymorphism and Method Overloading:

# (((((((((((((  Polymorphism: ))))))))))))) 
# Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
# It enables you to use objects of different classes interchangeably if they have a common interface 
# (methods with the same name).

# (((((((((((((( Method Overloading: )))))))))))))) 
# Method overloading is a feature that allows a class to have multiple 
# methods with the same name but different parameters. Python does not support traditional method overloading,
# but you can achieve similar behavior using default parameter values.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def add(a, b):
        return a+b
    
    def add(a, b):
        return a+b+1

    def add(a, b):
        return a+b+3
    
    def add(a, b, c):
        return a+b+c


shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
    
# Circle and Square are subclasses of Shape.
# Both subclasses implement the area method.
# We demonstrate polymorphism by calling the area method on different objects.



s = Square(4)

# This example shows that when we try to create more than one method with same name in the same 
# class it will not throw any error but it will execute the last method 
# which were having the exact same name

# Don't try to create the object first and then call the method which is not taking self as the first parameter 
# It will throw error that the method require only 2 parameters but 3 provided and the 3rd parameter was the self
# which was included while creating the object

# Since, python doesn't supports method overloading it will execute the last method with same name only 
# and throws this error
# print(Square.add(1, 3))  # TypeError: Square.add() missing 1 required positional argument: 'c'


print(Square.add(1, 2, 3))