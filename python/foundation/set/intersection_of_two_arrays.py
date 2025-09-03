#LINK: https://leetcode.com/problems/intersection-of-two-arrays/description/

#ONE LINE SOLUTION. 
# Convert nums1 and nums2 to sets (removing duplicates), & creates a new set with elements common to both, 
# list() converts that new set into a list
#return list(set(nums1) & set(nums2))

#Alternate solution for more clarity
from typing import List 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #add nums1 to hashset
        hashset = set(nums1)
        #take intersection list
        intersection = []
        #for each num in nums2, if in hashset append to list and remove from set(unique combination required)
        for num in nums2:
            if num in hashset:
                intersection.append(num)
                hashset.remove(num)
        return intersection

#TC: O(N + M) : set() iterates through each element in nums1 and adds to set O(N), num iterates through each 
# element in nums2 O(M)
#SC: O(N) : hashset takes nums1 lenght in worst case and intersection will always be <= hashset size