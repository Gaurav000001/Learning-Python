# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"



def getFibonacciSequenceTillN(n):
    if n < 0 or n == 0:
        return []
    if(n == 1):
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n, 1):
        fib.append(fib[i-1]+fib[i-2])

    return fib


n = 5
arr = getFibonacciSequenceTillN(n)

print(arr)


