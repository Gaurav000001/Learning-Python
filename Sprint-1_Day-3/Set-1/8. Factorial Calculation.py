# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."


def facto(n):
    if n == 1:
        return n
    
    return n * facto(n-1)


integer = 5
factorial = facto(integer)

print(f"Factorial of {integer} is {factorial}")