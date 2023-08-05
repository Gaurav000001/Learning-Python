### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

# **Given**:

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# Expected output:

# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}



employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Inbuild approach
Dict = dict.fromkeys(employees, defaults)
print(Dict)


# Iteration approach
Dict2 = dict()
for e in employees:
    Dict2[e] = defaults
print(Dict2)