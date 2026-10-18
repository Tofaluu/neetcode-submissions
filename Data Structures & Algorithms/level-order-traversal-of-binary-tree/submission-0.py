# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        order = []
        queue = deque([root])
        length = 1
        nextLevelLength = 0

        while queue:
            currentLevel = []

            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    nextLevelLength += 1
                if node.right:
                    queue.append(node.right)
                    nextLevelLength += 1
                currentLevel.append(node.val)

            order.append(currentLevel)
            length = nextLevelLength
            nextLevelLength = 0
        
        return order




        
