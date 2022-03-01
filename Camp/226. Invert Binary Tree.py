# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(root, r1):
            
            if not r1:
                return
            
            if not root:
                root = r1
                
            temp = r1.left
            r1.left = r1.right
            r1.right = temp
            
            invert(root, r1.left)
            invert(root, r1.right)
            return root
        return invert(None, root)
            
            
        
