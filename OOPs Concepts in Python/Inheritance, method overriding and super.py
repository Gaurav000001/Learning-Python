# (((((((((((((  Inheritance: ))))))))))))) 
# Inheritance allows a new class (the derived class or subclass) to inherit 
# attributes and methods from an existing class (the base class or superclass). 
# This promotes code reuse and helps in creating a hierarchy of classes.

# ((((((((((((  Method Overriding: )))))))))) 
# Method overriding is the practice of providing a specific implementation for 
# a method in a subclass that is already defined in its superclass. This allows the subclass to customize 
# or extend the behavior of the inherited method.


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!






# Using super() to Call Parent Class Methods:

# The super() function is used to call a method from the parent class. 
# It allows you to access and call methods that have been overridden in the subclass.

class Parent:
    
    name = "Parent"
    
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print("Parent's display method")

class Child(Parent):
    
    def __init__(self, name):
        # Child constructor should fullfill the need of the parent default constructor
        super().__init__(name)
    
    def display(self):
        super().display()
        print("Child's display method")
        
        # Accessing the parent class variable using super() method
        parentName = super().name
        print(parentName)
        

child = Child("child")
child.display()


