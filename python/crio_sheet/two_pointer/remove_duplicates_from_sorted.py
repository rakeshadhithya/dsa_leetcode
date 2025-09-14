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

#TC: O(N) : right iterates through each number O(N), left moves till right (negligible)
#SC: O(1) : no extra space
