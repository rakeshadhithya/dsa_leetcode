#LINK: https://leetcode.com/problems/contains-duplicate/

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #add elements to set and compare lengths
        return len(set(nums)) != len(nums)
#TC: O(N) : set() function traverses each element of nums
#SC: O(N) : set object stores all elements of nums in worst case 