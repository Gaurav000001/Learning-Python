# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

# Reversing the string using for loop
def reverseString(str):
    bag = ""
    for c in str:
        bag = c + bag

    return bag


reversed = reverseString("Python")
print(reversed)


#Reversing the string using inbuild function
def reverseStringWithInbuildFunction(s):
    return s[::-1]

reversedString = reverseStringWithInbuildFunction("Python")
print(reversedString)