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

#iterative solution
def tribonacci_iterative(n):
    trib = [0, 1, 1]
    for i in range(2, n+1):
        trib[i] = trib[i-1] + trib[i-2] + trib[i-3]
    return trib[n]
#TC: O(N) : i iterates through each num till n
#SC: O(N) : trib list stroes each number in trib series till n

