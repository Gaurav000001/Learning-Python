# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."



# Create a list of numbers from 1 to 10
list = list(range(1, 11))
print("Original list:", list)

# Add a number (20) to the list
list.append(20)
print("List after adding 20:", list)

# Remove a number (3) from the list
list.remove(3)
print("List after removing 3:", list)

# Sort the list in ascending order
list.sort()
print("Sorted list:", list)