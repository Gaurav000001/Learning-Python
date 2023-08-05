### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# str1 = PyNaTive

# Expected Output:

# yaivePNT

def reArrange(s):
    arr = [char for char in s]

    j = 0
    for i in range(0, len(arr)):
        if arr[i].islower():
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1

    return "".join(arr)


print(reArrange("PyNaTive"))