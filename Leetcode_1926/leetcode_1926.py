class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # maze.reverse()
        list = ['up', 'down', 'left', 'right']
        deq = deque()
        visited = set()
        m = len(maze)
        n = len(maze[0])
        cur_row = entrance[0]
        cur_col = entrance[1]
        steps = 0
        deq.append(([cur_row, cur_col], steps))
        visited.add((cur_row, cur_col))
        while deq:
            [cur_row, cur_col], steps = deq.popleft()
            for direction in list:
                if direction == 'down':
                    if cur_row + 1 == m:
                        continue
                    if maze[cur_row+1][cur_col] == '+':
                        continue
                    if (cur_row+1, cur_col) not in visited and (cur_row+1 == 0 or cur_row+1 == m - 1 or cur_col == 0 or cur_col == n - 1):
                        return steps + 1
                    if (cur_row+1,cur_col) not in visited:
                        deq.append(([cur_row+1, cur_col], steps+1))
                        visited.add((cur_row+1, cur_col))
                if direction == 'up':
                    if cur_row -1 == -1:
                        continue
                    if maze[cur_row-1][cur_col] == '+':
                        continue
                    if (cur_row-1, cur_col) not in visited and (cur_row-1 == 0 or cur_row-1 == m - 1 or cur_col == 0 or cur_col == n - 1):
                        return steps + 1
                    if (cur_row-1, cur_col) not in visited:
                        deq.append(([cur_row-1, cur_col], steps+1))
                        visited.add((cur_row-1, cur_col))
                if direction == 'left':
                    if cur_col - 1 == -1:
                        continue
                    if maze[cur_row][cur_col - 1] == '+':
                        continue
                    if (cur_row, cur_col-1) not in visited and (cur_col-1 == 0 or cur_col-1 == n - 1 or cur_row == 0 or cur_row == m - 1):
                        return steps + 1
                    if (cur_row, cur_col -1) not in visited:
                        deq.append(([cur_row, cur_col-1], steps+1))
                        visited.add((cur_row, cur_col-1))
                if direction == 'right':
                    if cur_col+1== n:
                        continue
                    if maze[cur_row][cur_col + 1] == '+':
                        continue
                    if (cur_row, cur_col+1) not in visited and (cur_col+1 == 0 or cur_col+1 == n - 1 or cur_row == 0 or cur_row == m - 1):
                        return steps + 1
                    if (cur_row, cur_col+1) not in visited:
                        deq.append(([cur_row, cur_col+1], steps+1))
                        visited.add((cur_row, cur_col+1))
        return -1