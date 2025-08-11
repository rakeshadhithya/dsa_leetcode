#find the factorial of given integer with recursion
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1) 

#TC: O(N) : each node O(1) total nodes N 
#SC: O(N) : each node O(1) depth N 