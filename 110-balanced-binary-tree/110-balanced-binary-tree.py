# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def height_calculate(root):
            if not root:
                return 0
            
            left = height_calculate(root.left)
            right = height_calculate(root.right)
            
            return 1 + max(left, right)
        
        if abs(height_calculate(root.left)-height_calculate(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)