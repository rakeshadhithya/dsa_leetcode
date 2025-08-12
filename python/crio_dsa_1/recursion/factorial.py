#find the factorial of given integer with recursion
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1) 

#TC: O(N) : each node O(1) total nodes N 
#SC: O(N) : each node O(1) depth N 

#iterative solution
def factorial_iterative(n):
    fact = [0, 1]
    for i in range(2, n+1):
        fact.append( i * fact[i-1])
    print(fact[n])
#TC: O(N) : i iterates through each number till n
#SC: O(N) : fact list stores each factorial of each number till n
    