# **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def twoSum(arr, t):
    s = 0
    e = len(arr)-1
    arr.sort()
    
    while(s < e):
        sum = arr[s] + arr[e]
        
        if sum == t:
            return [s, e]
        elif sum < t:
            s += 1
        else:
            e -= 1
            
    return "not found"


arr = [2, 7, 11, 15]
target = 9
print(twoSum(arr, target))