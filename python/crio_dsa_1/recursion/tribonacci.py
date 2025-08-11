#find the nth tribonacci term
def tribonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

#TC: O(3^N) : each Node O(1) total Nodes(3^N)
#SC: O(N) : each Node O(1) depth(N)

