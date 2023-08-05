# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."


def checkPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1, 1):
        
        if num%i == 0:
            return False
        
    return True

number = 13
isPrime = checkPrime(number)

if isPrime:
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")
