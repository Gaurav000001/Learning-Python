# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


def checkPalindrome(s):
    
    list = [char for char in s]
    
    i = 0
    j = len(list)-1
    for e in range(int(len(list)//2)):
        if list[i] != list[j]:
            return False
        else:
            i += 1
            j -= 1
            
    return True
    

str = "racecar"
print(checkPalindrome(str))