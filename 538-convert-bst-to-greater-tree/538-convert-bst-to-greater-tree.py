# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        curr_sum = 0
        def inorder(node):
            nonlocal curr_sum
            if not node: return 
            inorder(node.right)
            curr_sum += node.val
            node.val = curr_sum
            inorder(node.left)
        inorder(root)
        return root