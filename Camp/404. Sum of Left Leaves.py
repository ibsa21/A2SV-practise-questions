# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right:
            return 0
        
        def traverse(root, is_left):
            
            if not root:
                return 0
            
            if is_left and  not root.left and not root.right:
                return root.val
            
            
            return traverse(root.left, True) + traverse(root.right, False)
        
        return traverse(root, root)
        
            
        
