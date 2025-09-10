#LINK: https://leetcode.com/problems/rotate-image/
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #reverse the rows in matrix
        matrix.reverse()
        #transpose of n*n matrix
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            
#TC: O(N * N) : matrix.reverse O(N) + matrix traversal of each cell O(N*N)
#SC: O(1) : no extra ref to store 

'''
transpose: for n*n you can do in place else you have to create a new list. 
matrix problems: always take a new dummy matrix so you can access by indices instead of doing appending to each
row and then appending each row to list
ALTERNATE SOLUTION: you can first find transpose and then reverse each row in that. but first reverse rows then transpose is efficient
'''