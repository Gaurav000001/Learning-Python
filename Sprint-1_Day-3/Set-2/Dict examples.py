# In Python, the dict() function is an inbuilt function that is used to create dictionaries. 
# It is one of the methods to create dictionaries along with dictionary literals (using curly braces {}) and 
# dictionary comprehension. The dict() function offers flexibility in creating dictionaries 
# from various data structures.

# Here are some common use cases of the dict() function:


# Creating a dictionary from two lists or tuples representing key-value pairs:
keys = ['name', 'age', 'city']
values = ['John', 30, 'New York']

my_dict = dict(zip(keys, values))
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}



# Creating a dictionary from a list of tuples representing key-value pairs:
data = [('name', 'John'), ('age', 30), ('city', 'New York')]

my_dict = dict(data)
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}



# Creating a dictionary with default values using the fromkeys() method:
keys = ['name', 'age', 'city']
default_value = 'Unknown'

my_dict = dict.fromkeys(keys, default_value)
print(my_dict)
# Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}



# Creating an empty dictionary:
my_dict = dict()
print(my_dict)
# Output: {}



student = {
"name": "Rahul",
"age": 23,
"nationality": "Indian",
"location": "Nainital",
"is_married": False,
"highest_degree": "Btech",
"pcm_marks": [12,45,78]
}

# Ist way to iterate in a python dictionary
for k in student:
  print(k,student[k])
  print("---------One key-value ends here--------")

# IInd way of iterating in a python dictionary
for k, v in student.items():
   print(k,":",v)