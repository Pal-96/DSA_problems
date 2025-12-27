class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deq = deque()
        visited = set()
        direction = ['up', 'down', 'right', 'left']
        oranges = 0
        m = len(grid)
        n = len(grid[0])
        for r in range (0,m):
            for c in range(0, n):
                if grid[r][c] == 2:
                    deq.append([r,c,0])
                    visited.add((r,c))
                if grid[r][c] == 2 or grid[r][c] == 1:
                    oranges+=1
        if oranges == 0 or len(visited) == oranges :
            return 0
        
        while deq:
            r,c, mins = deq.popleft()
            for dir in direction:
                if dir == 'up':
                    if r-1 == -1:
                        continue
                    if grid[r-1][c] == 1:
                        grid[r-1][c] = 2
                        visited.add((r-1,c))
                        deq.append((r-1, c, mins+1))
                if dir == 'down':
                    if r+1 == m:
                        continue
                    if grid[r+1][c] == 1:
                        grid[r+1][c] = 2
                        visited.add((r+1,c))
                        deq.append((r+1, c, mins+1))
                if dir == 'right':
                    if c+1 == n:
                        continue
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        visited.add((r, c+1))
                        deq.append((r, c+1, mins+1))
                if dir == 'left':
                    if c-1 == -1:
                        continue
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        visited.add((r, c-1))
                        deq.append((r, c-1, mins+1))
            if len(visited) == oranges:
                if len(visited) == 1:
                    return mins
                return mins+1

        return -1