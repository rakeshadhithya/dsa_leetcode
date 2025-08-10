#LINK: https://leetcode.com/problems/search-insert-position/

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #take pointers left and right
        left = 0
        right = len(nums) - 1
        #until left <= right  (= important here to confirm every index is checked)
        while left <= right:
            #take mid
            mid = (left + right) // 2
            #check target = < or > and change left or right accordingly
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        #if not found then left is the position to insert
        return left
#TC: O(logN) : left and right poiters move dividing the array into half and not through each element
#while iterating or recursion depth depends on step, start and end. if step(k) is add/substract then N-b/k. 
#if step(k) is multiplying/dividing then logk(N-b)
#SC: O(1) : only constant spaces are taken