#LINK: https://leetcode.com/problems/container-with-most-water/

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        #two pointers from left and right, until not overlap
        left = 0
        right = len(height) - 1
        while left < right:
        #update max area min(h(l), h(r)) * r - l, move the pointer with low height
            max_area = max( max_area, min(height[left], height[right]) * (right - left) )
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
#TC: O(N) : left and right together iterate through each element. max, min takes O(1)
#SC: O(1) : all references store in O(1)
'''
0  1  2  3  4  5  6  7  8
1  8  6  2  5  4  8  3  7
               l  r
ma = 49

8  7  2  1
l  r
ma = 7
'''
        