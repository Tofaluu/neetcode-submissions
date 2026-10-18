class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hash = {i : set() for i in range(n)}
        visited = set()
        count = 0
        for edge in edges:
            hash[edge[0]].add(edge[1])
            hash[edge[1]].add(edge[0])
        
        def dfs(visited, current):
            if current in visited:
                return
            else:
                visited.add(current)
                for child in hash[current]:
                    dfs(visited, child)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(visited, i)
        
        return count

