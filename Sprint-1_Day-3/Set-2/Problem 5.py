### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. 
# Create a new list that contains the 0th index item from both the list, 
# then the 1st index item, and so on till the last element. 
# any leftover items will get added at the end of the new list.

# **Given**:

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# Expected output:

# ['My', 'name', 'is', 'Kelly']


def concatToListsIndexWise(list1, list2):
    
    list3 = []
    i = 0
    j = 0

    while(i < len(list1) and j < len(list2)):
        list3.append(list1[i] + list2[j])
        i += 1
        j += 1

    if i < len(list1):
        list3 = list3 + list1[i:]

    if j < len(list2):
        list3 = list3 + list2[j:]

    return list3


list1 = ["M", "na", "i", "Ke", "and", "what", "do", "you", "want"]
list2 = ["y", "me", "s", "lly"]

list3 = concatToListsIndexWise(list1, list2)

print(list3)