# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, 
# handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."


def divide(dividant, divisor):
    try:
        return dividant/divisor
    except ArithmeticError as e:
        return "Error: ", e
    
    
print(divide(5, 0))