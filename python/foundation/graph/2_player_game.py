#finds best position to move based on max_value and not visited
def best_pos(r, c, grid, visited):
    max_val = -float('inf')
    max_pos = None
    for dr,dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and visited[nr][nc] == False:
            if grid[nr][nc] > max_val:
                max_val = grid[nr][nc]
                max_pos = (nr,nc)
    return max_pos

def solve(grid):
    tr, tc = len(grid), len(grid[0])
    #create visited grid
    visited = [[False] * tc for r in range(tr)]
    #player 1 starts at first cell, player 2 at last cell
    x1, y1 = 0, 0
    visited[x1][y1] = True
    p1_scr = grid[x1][y1]
    x2, y2 = tr - 1, tc - 1
    visited[x2][y2] = True
    turn = 1
    while 1:
        #player 1's turn
        if turn == 1:
            move_pos = best_pos(x1, y1, grid, visited) 
            if move_pos == None:
                return p1_scr
            x1, y1 = move_pos
            visited[x1][y1] = True
            p1_scr += grid[x1][y1]
            turn = 2
        #player 2's turn
        else:
            move_pos = best_pos(x2, y2, grid, visited)
            if move_pos == None:
                turn = 1
                continue
            x2, y2 = move_pos
            visited[x2][y2] = True
            turn = 1
    #return p1_scr
#read matrix
matrix = []
try:
    while(1):
        line = input('Enter rows with numbers until ctrl + z: \n')
        row = [int(x) for x in line.split()]
        matrix.append(row)
except:
    print('Entered matrix is:')
    for r in matrix:
        print(r)
    p1_scr = solve(matrix)
    print(f'Maximum score player 1 can achieve is: {p1_scr} ')


#here we don't need to explore full path for each move, we just have to pick best move. that's why greedy instead of bfs