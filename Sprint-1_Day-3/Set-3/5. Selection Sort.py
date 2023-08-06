# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"



def selectionSort(list):
    
    for i in range(len(list)):
        
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
                
        list[i], list[minIndex] = list[minIndex], list[i]
        

list = [64, 25, 12, 22, 11]
print(list)
selectionSort(list)
print(list)
        












[64, 25, 12, 22, 11]
