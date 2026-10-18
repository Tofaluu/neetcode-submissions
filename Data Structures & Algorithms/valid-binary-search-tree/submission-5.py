# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = set()
        def recursiveValidBST(root: Optional[TreeNode], low, high):
            if not root:
                return True
            elif root.val in values or low > root.val or high < root.val:
                return False
            else:
                values.add(root.val)
                if root.left and root.val <= root.left.val:
                    return False
                if root.right and root.val >= root.right.val:
                    return False
                return recursiveValidBST(root.left, low, root.val) and recursiveValidBST(root.right, root.val, high)

        return recursiveValidBST(root, -1000000001, 1000000001)