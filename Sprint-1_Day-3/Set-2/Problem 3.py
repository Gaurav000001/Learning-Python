### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# s1 = "Ault"
# s2 = "Kelly"

# Expected Output:

# AuKellylt


# def getMiddleOf(str):
#     if len(str)%2 == 0:
#         return (len(str)/2) + 1
#     else:
#         return int((len(str)+1)/2)
    

#Inbuild function approach
def appendAtMiddle(str1, str2):
    # n = getMiddleOf(str1)

    mid_index = len(str1)//2 if len(str1)%2 == 0 else (len(str1)//2)+1

    str3 = str1[:mid_index] + str2 + str1[mid_index:]

    return str3

# for loop approach
def appendAtMiddle2(str1, str2):

    mid_index = len(str1)//2 if len(str1)%2 == 0 else (len(str1)//2)+1

    str3 = ""
    for index, char in enumerate(str1):
        if(index == mid_index):
            str3 += str2

        str3 += char

    return str3


s1 = "Ault"
s2 = "Kelly"
print(appendAtMiddle2(s1, s2))