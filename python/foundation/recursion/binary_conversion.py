#convert the given integer to binary string 
def binary(n):
    #if n < 2 return str of n. combines if n==1 return '1' and n==0 return '0'
    if n < 2:
        return str(n)
    #return ans(n//2) + remainder n % 2
    return binary(n//2) + str(n%2)      

#TC: O(log2(N)) : each node O(1) total Nodes O(log2(N))
#SC: O(log2(N)) : each node O(1) depth O(log2(N))  


# 10 % 2 = 0, 10 // 2=5
# 5 % 2 = 1, 5 // 2 = 2
# 2 % 2 = 0, 2 // 2 = 1
# 1 % 2 = 1, 1 // 2 = 0

#iterative
def binary_iterative(n):
    binary_str = ''         #instead of array we directly took str
    while n != 0:
        binary_str = str(n%2) + binary_str    
        n //= 2
    return binary_str

n = 100
print(binary(n))
print(binary_iterative(n))
#TC: O(log2(N)) : n becomes half in each iteration
#SC: O(N) : binary_str stores digits compared to the size of input

'''
In both of the above solutions we are adding remainder from last, 
so we don't need reversal step before returning, but you can add from first, at last reverse and return
'''