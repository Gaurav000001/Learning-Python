# ((((((((((((  Constructors:  ))))))))))))
# A constructor is a special method that gets called when an object of a class is instantiated. 
# It initializes the object's attributes and performs any necessary setup.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25

# The __init__ method is the constructor.
# It initializes the name and age attributes for each person object.








# ((((((((((((  Instance Variables:  ))))))))))))

# Instance variables (also known as instance attributes) are variables that belong to individual instances 
# of a class. They store data specific to each object.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.make)  # Output: Toyota
print(car2.model) # Output: Civic

# make and model are instance variables.
# Each car object has its own values for these variables.







# ((((((((((((((((  Access Modifiers in Python:  ))))))))))))))))

# Access modifiers are keywords that determine the visibility and accessibility of attributes and 
# methods within a class. They help control the level of encapsulation and data hiding in your classes.

# 1. Public (public):

# Attributes/methods with no leading underscores are considered public.
# Public attributes/methods can be accessed from anywhere, both within and outside the class.
# They are meant to be used freely and do not provide data hiding.


# Protected (protected):

# Attributes/methods with a single leading underscore (_) are considered protected.
# Protected attributes/methods can be accessed from within the class and its subclasses.
# They are a convention to indicate that the attribute/method is for internal use and should not be accessed 
# directly from outside.


# Private (private):

# Attributes/methods with a double leading underscore (__) are considered private.
# Private attributes/methods can only be accessed from within the class they are defined in.
# They are used for data hiding and are not meant to be accessed directly from outside the class.


class BankAccount:
    def __init__(self):
        self.balance = 0           # Public attribute
        self._account_type = "Savings"  # Protected attribute
        self.__account_number = "12345"  # Private attribute

    def deposit(self, amount):
        self.balance += amount

    def _get_account_type(self):
        return self._account_type

    def __get_account_number(self):
        return self.__account_number

account = BankAccount()

# Public attributes/methods can be accessed directly
account.deposit(1000)
print(account.balance)  # Output: 1000

# Protected attributes/methods can be accessed within the class and subclasses
print(account._get_account_type())  # Output: Savings

# Private attributes/methods cannot be accessed directly
# print(account.__account_number)  # Uncommenting this line will raise an error.
