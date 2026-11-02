# O(m * n) time and space complexity
# a solution could be: using bfs/queue to keep track of current rotten fruits to explore
# at each step, explore neighbours, append to queue if a fresh fruit

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minute = 0


        queue = deque([(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2])

        while queue:
            rotted = False
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (r < rows - 1):
                    if grid[r + 1][c] == 1:
                        queue.append((r + 1, c))
                        grid[r + 1][c] = 2
                        rotted = True
                if (r > 0):
                    if grid[r - 1][c] == 1:
                        queue.append((r - 1, c))
                        grid[r - 1][c] = 2
                        rotted = True
                if (c < cols - 1):
                    if grid[r][c + 1] == 1:
                        queue.append((r, c + 1))
                        grid[r][c + 1] = 2
                        rotted = True
                if (c > 0):
                    if grid[r][c - 1] == 1:
                        queue.append((r, c - 1))
                        grid[r][c - 1] = 2
                        rotted = True
            if rotted:
                minute += 1
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return minute