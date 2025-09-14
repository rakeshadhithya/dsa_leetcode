#LINK: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st = set(nums)
        return [x for x in range(1, len(nums)+1) if x not in st]
#TC: O(N) : st creation O(N), list comprehesion O(N) bcoz set lookup takes O(1)
#SC: O(N) : st stores N elements in worst case O(N)


#EFFICIENT SOLUTION
'''
each number tells which index they belong to. for each number make its index's value to negative. 
after that find which indices store postive values
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            #abs becoz this num can be already made negative
            i = abs(n) - 1
            nums[i] = - abs(nums[i])
        return [i+1 for i,v in enumerate(nums) if v > 0]
#TC: O(N) : n iterates through each element O(N) + return's list comprehension O(N)
#SC: O(1) : ignoring return list