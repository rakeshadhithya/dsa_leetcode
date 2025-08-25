#LINK: https://leetcode.com/problems/majority-element/

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #APPROACH 1: same like voting, votes and candidate cancel out and one will be winner(>n//2 guarenteed)
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if candidate == n else -1)
        return candidate
        
#TC: O(n) : n iterates through each num in nums
#SC: O(1) : count, candidate takes O(1)
'''
Think of each element as a vote.
When candidate and other elements "fight," their counts cancel each other out.
Because the majority element has more than half the votes, it cannot be fully canceled. It always survives to the end.
'''
'''
#APPROACH 2: sorting, when sorted element appeared > n//2 will always be in middle
nums = sorted(nums)
return nums[len(nums)//2]
TC: O(NlogN) : sorted function take O(NlogN)
SC: O(N) : nums store sorted list

#APPROACH 3: COUNT AND FIND MAX
        #can be easily converted to java, additional checks when counting
        majority = nums[0]
        max_freq = 1
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > max_freq:
                max_freq = d[n]
                majority = n
        return majority
        #in python, majority = max(d, key=d.get)  # C-level speed
#TC: O(N) : n iterates through each element in nums
#SC: O(N) : d stores all elements and its freq's
'''