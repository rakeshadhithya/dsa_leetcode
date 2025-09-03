#LINK: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left+1

#TC: O(N) : right iterates through all elements in list O(N), left moves only 1 at a time O(1)
#SC: O(1) : no extra space O(1)
'''
keep left pointer at 1st elemnt
from right from next till end
if left element and right element same move right, else move left replace with right's element(instead of moving rightin extra loop inside right loop and keeping null checks and all just move left, right already moves)
return left + 1
1, 2, 2
   l   r
'''