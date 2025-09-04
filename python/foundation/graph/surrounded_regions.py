#LINK: https://leetcode.com/problems/surrounded-regions/

from typing import List
class Solution:
    def dfs(self, board, r, c, tr, tc):
        #if row, col out of range of not O return, else mark s and do same for surrounding
        if r < 0 or r >= tr or c < 0 or c >= tc or board[r][c] != 'O':
            return
        board[r][c] = 'S'
        for dr, dc in [(-1, 0), (1, 0), (0,-1), (0, 1)]:
            self.dfs(board, r+dr, c+dc, tr, tc)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        tr, tc = len(board), len(board[0])
        #from left and right cols, mark safe O's using dfs
        for r in range(tr):
            self.dfs(board, r, 0, tr, tc )
            self.dfs(board, r, tc-1, tr, tc)
        #from top and bottom rows, mark safe O's using dfs
        for c in range(tc):
            self.dfs(board, 0, c, tr, tc)
            self.dfs(board, tr-1, c, tr, tc)
        
        #traverse and make O's to X's and S's to O's
        for r in range(tr):
            for c in range(tc):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'


        



'''
def dfs(matrix, r, c, tr, tc):
    #if r,c out of boudaries or not O return else make it S and do same for surrounding cells
    if r < 0 or r >=tr or c < 0 or c >= tc or matrix[r][c] != 'O':
        return
    matrix[r][c] = 'S'
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(matrix, r+dr, c+dc, tr, tc)

def solve(matrix):
    tr, tc = len(matrix), len(matrix[0])
    #for left and right cols, mark safe O's
    for r in range(tr):
        dfs(matrix, r, 0, tr, tc)
        dfs(matrix, r, tc-1, tr, tc)
    #for top and bottom rows, mark safe O's
    for c in range(tc):
        dfs(matrix, 0, c, tr, tc)
        dfs(matrix, tr-1, c, tr, tc)

    #iterate matrix and make O to X and S to O
    for r in range(tr):
        for c in range(tc):
            if matrix[r][c] == 'O':
                matrix[r][c] = 'X'
            if matrix[r][c] == 'S':
                matrix[r][c] = 'O'

#read matrix
matrix = []
try:
    while(1):
        line = input('Enter rows with either \'O\' or \'S\' until ctrl + z: \n')
        row = line.split()
        matrix.append(row)
except:
    for r in matrix:
        print(r)
    solve(matrix)
    print()
    print('After Solving:  ')
    for r in matrix:
        print(r)


PS D:\coding\ssssdp\homeworks\sethubatch2dataengnieer> & "C:/Program Files/Python311/python.exe" d:/coding/ssssdp/homeworks/sethubatch2dataengnieer/graph_probs.py
Enter rows with either 'O' or 'S' until ctrl + z: 
X X X X X
Enter rows with either 'O' or 'S' until ctrl + z: 
X O O X O
Enter rows with either 'O' or 'S' until ctrl + z: 
X X O X O
Enter rows with either 'O' or 'S' until ctrl + z: 
X O X O X
Enter rows with either 'O' or 'S' until ctrl + z: 
O O O X X
Enter rows with either 'O' or 'S' until ctrl + z: 
^Z
['X', 'X', 'X', 'X', 'X']
['X', 'O', 'O', 'X', 'O']
['X', 'X', 'O', 'X', 'O']
['X', 'O', 'X', 'O', 'X']
['O', 'O', 'O', 'X', 'X']

After Solving:
['X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'O']
['X', 'X', 'X', 'X', 'O']
['X', 'O', 'X', 'X', 'X']
['O', 'O', 'O', 'X', 'X']

'''

