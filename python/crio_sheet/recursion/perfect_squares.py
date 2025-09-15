#LINK: https://leetcode.com/problems/perfect-squares/

#DYNAMIC PROGRAMMING ITERATIVE
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
# TC: O(n * sqrt(n)) : for each i up to n, check all squares ≤ i
# SC: O(n) : DP array of size n+1

#RECURSIVE WITH MEMOIZATION
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def helper(self, k):
        if k == 0:
            return 0
        ans = float('inf')
        j = 1
        while j * j <= k:
            ans = min( ans, self.helper(k - j * j) + 1 )
            j += 1
        return ans
    def numSquares(self, n: int) -> int:
        return self.helper(n)
# TC: O(n * sqrt(n)) : each state 0..n solved once, each tries up to √n squares
# SC: O(n) : memoization cache + recursion depth

'''
For each number, subtract each possible square, look up the best solution for the smaller number(number after subtraction) 
and add 1 for this subtracted square , and take the minimum.
@lru_cache(None) = “Memoize this function, cache every result, never recompute the same argument twice.
'''