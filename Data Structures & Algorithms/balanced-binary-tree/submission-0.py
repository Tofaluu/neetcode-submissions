# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(current):
            if not current:
                return 0
            else:
                return 1 + max(height(current.left), height(current.right))

        def recursive(current):
            if not current:
                return True
            else:
                left_height = height(current.left)
                right_height = height(current.right)

                if abs(left_height - right_height) > 1:
                    return False
                
                return recursive(current.left) and recursive(current.right)
        
        return recursive(root)