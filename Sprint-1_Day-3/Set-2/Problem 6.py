# Problem 6: Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


def convert(list1, list2):
    
    result = []

    for i in list1:
        for j in list2:
            # result.append("{} {}".format(i,j))
            # result += [f"{i} {j}",]
            # result.extend([f'{i}{j}',])
            result.append(i + j)

    return result



list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = convert(list1, list2)

print(result)