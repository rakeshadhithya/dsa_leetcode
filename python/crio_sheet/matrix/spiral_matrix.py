#LINK: https://leetcode.com/problems/spiral-matrix/

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        #boundaries
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        #until both left, right and top, bottom overlap
        while left <= right and top <= bottom:
            #from left to right traverse along top, increment top
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            #from top to bottom traverse along right, decrement right
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            #if top didn't overlap, from right to left traverse along bottom, decrement bottom
            if top <= bottom:
                
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            #if left didn't overlap, from bottom to top traverse along left, increment left
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result
#TC: O(N * M) : we traverse each cell once
#SC: O(N * M) : we store each cell value in a list