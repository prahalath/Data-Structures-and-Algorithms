from collections import deque

def rottingOranges(grid):
    m = len(grid)
    n = len(grid[0])
    fresh_count = 0
    level = 0
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    queue = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] == 1:
                fresh_count += 1
    print (fresh_count)
    print (queue)   
    
    while queue:
        level += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for dx, dy in dirs:
                new_i = i + dx
                new_j = i + dy
                if 0 <= new_i < m and 0 <= new_j < n:
                    if grid[new_i][new_j] == 1:
                        fresh_count -= 1
                        grid[new_i][new_j] = 2
                        queue.append((new_i, new_j))
                        print (queue)
    return -1 if fresh_count != 0 else max(level-1, 0)

grid = [[2,1,1],[1,1,0],[0,1,1]]
print (rottingOranges(grid))