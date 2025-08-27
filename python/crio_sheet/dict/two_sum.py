#LINK: https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use dict, if compliment not in map add curr num and its index to map, if compliment in map return ans(compliment index and curr index)
        d = {}
        for i, n in enumerate(nums):
            if target - n not in d:
                d[n] = i
            else:
                return[d[target-n], i]
#TC: O(N) : i, n iterates through each number in nums
#SC: O(N) : d stores all elements in worst case O(N)

#ALTERNATE APPROACH:
#Use brute force, for each element, find if complement is there from its next till end