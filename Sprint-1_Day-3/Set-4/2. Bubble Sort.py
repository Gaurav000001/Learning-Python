# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"


def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
    return list


list = [64, 34, 25, 12, 22, 11, 90]
print("Original List: {}".format(str(list)))

bubbleSort(list)
print("Sorted List {}".format(str(list)))