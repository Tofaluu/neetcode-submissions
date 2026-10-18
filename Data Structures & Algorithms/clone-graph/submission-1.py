"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        old_to_new = {}
        old_to_new[node] = Node(node.val)
        start_node = node
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor in old_to_new:
                    old_to_new[curr].neighbors.append(old_to_new[neighbor])
                else:
                    queue.append(neighbor)
                    newNeighbor = Node(neighbor.val)
                    old_to_new[neighbor] = newNeighbor
                    old_to_new[curr].neighbors.append(newNeighbor)

        return old_to_new[start_node]