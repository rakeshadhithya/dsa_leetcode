#LINK: https://leetcode.com/problems/set-matrix-zeroes/

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #check if any zero in first row and first col(we are using them as marker and we might override them)
        zero_in_firstcol = any(matrix[row][0] == 0 for row in range(len(matrix)))
        zero_in_firstrow = any(matrix[0][col] == 0 for col in range(len(matrix[0])))
        #2. traverse matrix excluding 1st row and col and if 0 make its row in the 1st col 0 and its col in the first row 0
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        #3. traverse matrix excluding first row and col(our markers should not disappear) 
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
            #if zero in first row for same col or if zero in first col for same row, make zero
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        #4. if zero in first row or col make all zero
        if zero_in_firstrow:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        if zero_in_firstcol:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        
#TC: O(M * N) : zero_in_firstcol O(M) + zero_in_firstrow O(N) + 2nd step O(M) * O(N) + 3rd step O(M) * O(N), 4th step O(M) + O(N)
#SC: O(1) : zero_in_firstcol and zero_in_firstrow stroes only 1 boolean, when iterating a generator atmost only 1 boolen is in memeory 
# as soon as true is found it returns true else false
'''
ALTERNATE APPROACHES
1. use two sets for adding row nos. for rows in which there is a zero, another for same as cols. for each row 
in set, make all cols zero, for each col in set make all rows zero
2. use a visit array, traverse matrix and create a copy array in which in place of zeros put float('inf'),
traverse matrix once again, if cell is float('inf') for same row make all cols zero, for same col make all rows zero
'''