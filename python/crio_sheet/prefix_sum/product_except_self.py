#LINK: https://leetcode.com/problems/product-of-array-except-self/
#EXCLUSIVE 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        suffix = 1
        #add exclusive prefix multiplication of each index to res
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        #before calculating suffix
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
    
#INCLUSIVE
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        suffix = 1
        #calculate prefix while adding to res
        for i in range(len(nums)):
            prefix *= nums[i]
            res[i] = prefix
        #before calculating suffix update res based on prefix and suffix till now
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                res[i] = suffix
            elif i == len(nums) - 1:
                res[i] = res[i-1]
            else:
                res[i] = res[i - 1] * suffix
            suffix *= nums[i]
        return res

#TC: O(N) : creation of res takes O(N) + in first loop i iterates in forward direction O(N) + in second loop i iterates 
# in reverse direction O(N)
#SC : O(N) : res stores as many elements as in nums O(N)