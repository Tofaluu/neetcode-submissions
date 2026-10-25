# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def recursive(current):
            nonlocal max_diameter
            if not current:
                return 0

            left_height = recursive(current.left)
            right_height = recursive(current.right)

            max_diameter = max(max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        recursive(root)
        return max_diameter