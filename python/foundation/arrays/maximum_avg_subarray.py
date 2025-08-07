#Link: https://leetcode.com/problems/maximum-average-subarray-i/
from typing import *
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         #find sum of initial window, initial ans is this
        total = sum(nums[:k])
        max_avg = total / k
        #slide the window, add right to sum move next, remove left from sum move next, update ans
        left = 0
        right = k
        while right < len(nums):
            total += nums[right]
            right += 1
            total -= nums[left]
            left += 1
            avg = total / k
            max_avg = max(avg, max_avg)
        return max_avg

#Alternate Solution(for fixed window you can use for loop):
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         #find sum of initial window, initial ans is this
        total = sum(nums[:k])
        max_total = total
        #slide the window, add right to sum move next, remove left from sum move next, update ans
        for i in range(k, len(nums)):
            total += (nums[i] - nums[i-k])
            max_total = max(total, max_total)
        return max_total/k
    
# TC: O(N) -> sum of k elements O(K), iterting from k to N O(N)
# SC: O(1) -> nums[:k] O(K)

