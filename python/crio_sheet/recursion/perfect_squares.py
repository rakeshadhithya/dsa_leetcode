#LINK: 
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)  #repetation is done in C and much faster than comprehension
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[ i - j * j] + 1)
                j += 1
        return dp[n]

'''
For each number i, try subtracting each possible square, look up the best solution for the smaller number(number after subtraction) 
and add 1 for this subtracted square , and take the minimum.
'''