# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        length = len(preorder)
        hash = {}
        for i in range(length):
            hash[inorder[i]] = i
        
        def recursive(preorder, inorder, pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            else:
                in_idx = hash[preorder[pre_start]]
                left_size = in_idx - in_start
                return TreeNode(preorder[pre_start], 
                recursive(preorder, inorder, pre_start + 1, pre_start + left_size, in_start, in_idx - 1), 
                recursive(preorder, inorder, pre_start + left_size + 1, pre_end, in_idx + 1, in_end))
        
        return recursive(preorder, inorder, 0, length - 1, 0, length - 1)

            

