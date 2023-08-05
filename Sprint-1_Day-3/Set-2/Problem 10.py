### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

tuple1 = (11, [22, 33], 44, 55)

# Expected output:

# tuple1: (11, [222, 33], 44, 55)


# Manual approach
# tuple1[1][0] = 222

# print(tuple1)

# Logical approach
for e in tuple1:
    if type(e) == list:
        e[0] = 222
        
print(tuple1)