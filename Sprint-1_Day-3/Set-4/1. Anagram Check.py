# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"


def anagramCheck(s1, s2):
    list1 = []
    list2 = []
    for e1, e2 in zip(s1, s2):
        if e1 != " ":
            list1.append(e1)
        if e2 != " ":
            list2.append(e2)
            
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    if list1 == list2:
        return True
    else:
        return False
    

s1 = "cinema"
s2 = "iceman"

result = anagramCheck(s1, s2)

if(result):
    print(f"Both String s1: {s1} and String s2: {s2} are anagrams.")
else:
    print("Not Anagrams")
        



