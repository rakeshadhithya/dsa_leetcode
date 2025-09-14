#LINK: https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
#TC: O(N+M) : creation of two sets O(N+M) + intersection O(min(N,M)) + converting into list O(K), K is no. of intersected nums
#SC: O(N+M) : two sets O(N+M) in worst case + intersection O(K) + converting into list O(K)


#ALTERNATE SOLUTIONS
#1. convert one list to a set1, take another set to store result, iterate other list and if num in set1 add to res set. 
# at last convert res set to list and return
'''
2. WITHOUT USING SET
- sort both lists. use two pointers within lenghts. if nums at pointers equal add num to res and move pointers, 
else move the pointer with strictly less value (because it can never match bigger value in sorted array)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(res)
'''