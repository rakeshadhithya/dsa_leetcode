from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0) #sentinal(guard), to remove all left over in stack when no more heights
        for i, h in enumerate(heights):
            #if current height is less, then stack top height(larger) ends
            while len(stack) != 0 and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max( max_area, height * width )
            stack.append(i)
        return max_area
# TC: O(n) : for loop O(n), each index pushed once O(n), each index popped once O(n)
# SC: O(n) : stack stores up to n indices, rest variables take O(1)


'''
if height smaller, keep popping all the bigger ones than this and update area of popped height to max. 
when this height became bigger add
'''

