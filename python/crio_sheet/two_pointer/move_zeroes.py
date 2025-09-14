#LINK: https://leetcode.com/problems/move-zeroes/

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for right in range(len(nums)):
        #if num not zero, increment left copy that num
            if nums[right] != 0:
                left += 1
                nums[left] = nums[right]
        #increment left and make remaining all num to 0
        left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1

#TC: O(N) :right traverses through each element O(N-K), left traverse through remaining elements O(K)
#SC: O(1) : no extra space

'''
l = -1
0, 1, 0, 3, 12, 0
                r
1  3 12  
'''