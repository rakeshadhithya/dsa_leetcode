#LINK: https://leetcode.com/problems/find-pivot-index/

from typing import List
#APPROACH 1:  USE SUM(nums)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i in range(len(nums)):
            if prefix == total - prefix - nums[i]:
                return i
            prefix += nums[i]
        return - 1
    
#TC: O(N) : sum(nums) takes O(N) + i iterates through each element O(N)
#SC: O(1) : all ref's constant space only O(1)


#APPROACH2 USE SUFFIX ARRAY (not useful but just for building intuition on prefix/suffix problems)
#EXCLUSIVE SUFFIX: no edge conditions required, [0] * n covers that
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        #build suffix array (exclusive)
        suffix_arr = [0] * n
        for i in range(n-2, -1, -1):
            suffix_arr[i] = suffix_arr[i+1] + nums[i+1]
        #before calculating prefix, check suffix an return ans
        prefix = 0
        for i in range(n):
            if prefix == suffix_arr[i]:
                return i
            prefix += nums[i]
        return -1

#TC: O(N) : creation of suffix_arr O(N) + first i iterates in reverse O(N) + sencond loop i iterates each num O(N)
#SC: O(N) : suffix_arr stores N elements O(N)


#INCLUSIVE SUFFIX: needs all the conditions to checks edge cases
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        #create either suffix or prefix array(i chose suffix)
        suffix_arr = [0] * n
        suffix_arr[n - 1] = nums[n - 1]
        for i in range(n-2, -1, -1):
            suffix_arr[i] = suffix_arr[i+1] + nums[i]
        
        #before calculating prefix, return ans based on prefix till previous and suffix of next
        prefix = 0
        for i in range(n):
            #if 1st element then check sum till next
            if i == 0 and suffix_arr[1] == 0:
                return 0
            #if last element then check sum till prev
            elif i == n - 1:
                if prefix == 0:
                    return n - 1
            elif prefix == suffix_arr[i+1]:
                return i
            prefix += nums[i]
        return -1
    





    
            
