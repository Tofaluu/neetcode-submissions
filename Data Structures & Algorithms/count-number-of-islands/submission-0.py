class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(pair):
            r, c = pair
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return 
            else:
                grid[r][c] = '0'
                dfs((r - 1, c))
                dfs((r + 1, c))
                dfs((r, c - 1))
                dfs((r, c + 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs((i, j))
        return count

                
