class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hash = {i : set() for i in range(n)}
        visited = set()
        
        for edge in edges:
            hash[edge[0]].add(edge[1])
            hash[edge[1]].add(edge[0])
        
        def dfs(current, parent):
            if current in visited:
                return False
            else:
                visited.add(current)
                for child in hash[current]:
                    if child == parent:
                        continue
                    if not dfs(child, current):
                        return False
                return True
        
        if not dfs(0, -1):
            return False
        for i in range(n):
            if i not in visited:
                return False
        return True

