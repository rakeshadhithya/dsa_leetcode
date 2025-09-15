#LINK: https://leetcode.com/problems/sort-colors/

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, curr = 0, len(nums) - 1, 0
        while curr <= right:
            if nums[curr] == 1:
                curr += 1
            elif nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1

#TC: O(N) : mid iterates through each char O(N), left and right does not iterate then move 1 step as per mid
#SC: O(1) : in place sorting O(1)

'''
three pointers left adds 0's, right from back add's 2, mid checks 0's, 2's and swaps with left or right, if 1 skips.
when 2, we didn't move curr, becase it is not processed and can be 0, 1, 2
'''
        