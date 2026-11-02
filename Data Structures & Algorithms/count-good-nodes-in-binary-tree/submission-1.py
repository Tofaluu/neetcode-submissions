# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS?
# either store a set appended and then discarded at each recursive step or keep a current max_value parameter?
from functools import cache
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        @cache
        def recursive(currentNode, max_val):
            nonlocal count
            if not currentNode:
                return
            else:
                if currentNode.val >= max_val:
                    count += 1
                    max_val = currentNode.val
                recursive(currentNode.left, max_val)
                recursive(currentNode.right, max_val)
        
        recursive(root, -101)
        return count
        
        