#LINK: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #initialise max1 and max2 to less than minimum value in constraints
        max1 = - 2 ** 31
        max2 = - 2 ** 31
        #from 1st to last num
        for num in nums:
            #if num > max1, update max1, max2
            if num > max1:
                max2 = max1
                max1 = num
            #elif num > max2, update max2
            elif num > max2:
                max2 = num
        #return max1-1 * max2-1
        return (max1 - 1) * (max2 - 1)