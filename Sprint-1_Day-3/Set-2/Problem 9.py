### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# # Keys to extract
keys = ["name", "salary"]

# Expected output:
    
# {'name': 'Kelly', 'salary': 8000}


Dict = dict()
Dict["name"] = sample_dict["name"]
Dict["salary"] = sample_dict["salary"]
print(Dict)

Dict2 = dict()
for e in keys:
    Dict2[e] = sample_dict.get(e, "Default value if not found")
print(Dict2)