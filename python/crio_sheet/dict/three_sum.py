#LINK: https://leetcode.com/problems/3sum/

#DICTIONARY/SET APPROACH (USEFUL WHEN FINDING INDEXES RATHER THAN DIRECT VALUES)
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -nums[i]
            st = set()
            for j in range(i+1, len(nums)):
                if target - nums[j] in st:
                    ans.add( ( nums[i], target - nums[j], nums[j] ) )
                st.add(nums[j])
        return [list(x) for x in ans]

#TC: O(N^2) : sorted() takes O(NlogN) +  i iterates through each num O(N) * j iterates from i + 1 to end O(N)
#SC: O(N^2) : ans stores triplets O(N^2), nums store a sorted array O(N), st stores each number from i+1 to end O(N)
'''
total number of triplets in a array of size N is N^3, but we are generating unique triplets meaning for each n, excluding
that remaining two so O(N^2)
'''

'''
SORTING AND BINARY SEARCH APPROACH
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                #if total too large, we need smaller no.
                if total > 0:
                    right -= 1
                #if total too small, we need a bigger no.
                elif total < 0:
                    left += 1
                #if total matched, add triplet and skip duplicate lefts and rights
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
'''