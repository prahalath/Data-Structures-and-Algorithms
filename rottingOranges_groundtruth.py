from collections import deque
from itertools import product
def orangesRotting(grid):
    m = len(grid)
    n = len(grid[0])
    fresh = 0
    level = 0
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    queue = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] == 1:
                fresh += 1

    print (fresh)
    print (queue)
    
    while queue:
        level += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in dirs:
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                    fresh -= 1
                    grid[x+dx][y+dy] = 2
                    queue.append((x+dx, y+dy))
                    print (queue)
    return -1 if fresh != 0 else max(level-1, 0)


grid = [[2,1,1],[1,1,0],[0,1,1]]
print (orangesRotting(grid))