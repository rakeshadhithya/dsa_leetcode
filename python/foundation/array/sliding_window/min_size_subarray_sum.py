#LINK: https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #initial window and it's ans's
        left = 0
        total = 0
        min_size = float('inf')
        #right from first to last element
        for right in range(len(nums)):
            #add right
            total += nums[right]
            #while total >= target, update ans, remove left
            while total >= target:
                min_size = min(min_size, right-left+1)
                total -= nums[left]
                left += 1
        # if min_size is same then not found return 0 else min_size
        return min_size if min_size != float('inf') else 0
    

#Alternate solution(better clarity, actual solving of sliding window using while loop and pointers)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #initial window and it's ans's
        left = right = 0
        total = 0
        min_size = len(nums) + 1
        #until right reaches end
        while right < len(nums):
            #while total < target keep adding right
            while right < len(nums) and total < target:
                total += nums[right]
                right += 1
            #while total >= target update ans(min that's why before removed) keep removing left,
            while left < len(nums) and total >= target:
                min_size = min(min_size, right - left)
                total -= nums[left]
                left += 1
        #if min_size remains same, means not found return 0 else return min_size
        return 0 if min_size == len(nums) + 1 else min_size
    
#TC: O(N) : right traverses each element O(N), left traverses each element till last in worst case O(N)
#SC: O(1) : no extra space compared to input
