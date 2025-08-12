#find the nth fibonacci term
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#TC: O(2^N) : each Node O(1) total Nodes 2^N
#SC: O(N) : each Node O(1) depth O(N) 

#iterative solution:
def fibonacci_iterative(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-1])
    return fib[n]
#TC: O(N) : i iterates through each number from 2 to n+1
#SC: O(N) : fib list fact list stores each factorial of each number till n