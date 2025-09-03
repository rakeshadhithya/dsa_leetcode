#LINK: https://leetcode.com/problems/magic-squares-in-grid/

from typing import List
class Solution:
    def check_magic_square(self, grid: List[List[int]], row: int, col: int) -> bool:
        #check for 1-9 in grid
        visited = set()
        for r in range(row, row+3):
            for c in range(col, col+3):
                num = grid[r][c]
                if num < 1 or num > 9 or num in visited:
                    return False
                visited.add(num)
        #common sum
        common_sum = grid[row][col] + grid[row][col+1] + grid[row][col+2]
        #check rows for common sum
        for i in range(row, row+3):
            if common_sum != grid[i][col] + grid[i][col+1] + grid[i][col+2]:
                return False
        #check cols for common sum
        for i in range(col, col+3):
            if common_sum != grid[row][i] + grid[row+1][i] + grid[row+2][i]:
                return False
        #check diagonals for common sum
        if common_sum != grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]:
            return False
        if common_sum != grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]:
            return False
        #After all checks, return true
        return True
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        #intial ans
        count = 0
        #since subgrid is 3*3 loop should run up to lengths - 2
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                if self.check_magic_square(grid, row, col):
                    count += 1
        return count
    
#TC: O(row*col) : row and col operate through each element in given matrix, check_magic_square function takes O(1)
# only becuase no matter the size of input it performs calculations on 3*3 only. 
#SC: O(1) : only constant spaces are taken