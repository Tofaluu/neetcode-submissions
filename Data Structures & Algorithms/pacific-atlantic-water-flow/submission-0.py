class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        answer = []

        def dfs(pair, prev_height, visited):
            r, c = pair
            if r < 0 or r >= rows or c < 0 or c >= cols or pair in visited or heights[r][c] < prev_height:
                return
            else:
                visited.add((pair))
                dfs((r - 1, c), heights[r][c], visited)
                dfs((r + 1, c), heights[r][c], visited)
                dfs((r, c - 1), heights[r][c], visited)
                dfs((r, c + 1), heights[r][c], visited)
                

                
        for i in range(rows):
            dfs((i, 0), -1, pacific_visited)
            dfs((i, cols - 1), -1, atlantic_visited)
        for j in range(cols):
            dfs((0, j), -1, pacific_visited)
            dfs((rows - 1, j), -1, atlantic_visited)
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific_visited and (i, j) in atlantic_visited:
                    answer.append([i, j])
        return answer



