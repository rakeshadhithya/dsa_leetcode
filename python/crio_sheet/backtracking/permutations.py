#LINK: https://leetcode.com/problems/permutations/



from typing import List
#ALTERNATE: RECURSIVE SOLUTION
class Solution:
    def find_permutations(self, nums):
        if len(nums) == 0:
            return [[]]
        res = []
        for i in range(len(nums)):
            for k in self.find_permutations(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + k)
        return res
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.find_permutations(nums)
    
# TC: O(n² × n!) 
# - n! permutations must be generated
# - each requires up to O(n) work for slicing and O(n) work to build new lists
# - total ~ O(n² × n!)
#
# SC: O(n × n!)
# - O(n) recursion depth
# - O(n × n!) space to store all permutations in the result list
