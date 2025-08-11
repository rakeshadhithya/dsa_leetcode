#find the nth fibonacci term
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#TC: O(2^N) : each Node O(1) total Nodes 2^N
#SC: O(N) : each Node O(1) depth O(N) 