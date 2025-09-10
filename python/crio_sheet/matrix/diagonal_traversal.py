#LINK: https://leetcode.com/problems/diagonal-traverse/
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        m, n = len(mat), len(mat[0])
        #for each diagonal, find start pos from top or right
        for d in range(m+n-1):
            if d < n:
                row, col = 0, d
            else:
                row, col = d - n + 1, n - 1
            #create temp list, traverse diagonal and add (increment row, decrement col )
            temp = []
            while row < m and col >= 0:
                temp.append(mat[row][col])
                row += 1
                col -= 1
            #reverse diagonal if % 2 = 0, else simply add to traversal
            if d % 2 == 0:
                temp.reverse()
            result.extend(temp)
        return result
#TC: O(M*N) : we traverse each cell once + reverse takes O(M) since a diagonal at max have M(totalrows) elements + 
# result.exted takes at max min(m,n) elements in a diagonal
#SC: O(M*N) : result stores all elements in matrix(M*N) +  temp stores at max min(m,n) elements

'''
formulas:
row + col = diagonal no.
total diagonals = rows+cols-1
for each diagonal:
traversing right to left: diagonal starts from either top row or right col
traversing left to right: diagonal starts from either left col or bottom row
for zigzag reverse %2 diagonal


important:
Variables declared inside if, for, while, try, etc. are all in the function's scope (or module scope if not inside a function).
Only functions, classes, and modules create a new scope.
'''