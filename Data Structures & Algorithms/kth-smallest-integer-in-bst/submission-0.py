# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = root.val
        queue = deque()
        def recursive(root):
            if not root:
                return
            else:
                recursive(root.left)
                queue.append(root)
                recursive(root.right)
        recursive(root)
        for i in range(k - 1):
            queue.popleft()
        return queue.popleft().val