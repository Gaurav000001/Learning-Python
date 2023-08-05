# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"



def countVowels(str):
    count = 0

    for c in str:

        c = c.lower()

        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1

    return count


vowelCount = countVowels("Gaurav")
print("Number of vowels:", vowelCount)



# Using inbuild function

def countVowels2(str):
    count = 0

    for c in str:

        # casefold() is used as str.equalsIgnoreCase()
        c = c.casefold() 

        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1

    return count

vowelCount = countVowels2("GaurAv")
print("Number of vowels:", vowelCount)