# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"

from typing import List

def longestCommonaPrefix(strs: List[str]) -> str:
    strs.sort()
    s1 = strs[0]
    s2 = strs[len(strs)-1]
    i = 0
    while i<len(s1) and i<len(s2):
        if s1[i] == s2[i]:
            i += 1
        else:
            break

    return s1[:i]




list = ["flower","flow","flight"]

print(longestCommonaPrefix(list))