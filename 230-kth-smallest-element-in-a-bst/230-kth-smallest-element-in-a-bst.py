# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = []
        def bst(root):
            
            if not root:
                return 
            
            bst(root.left)
            result.append(root.val)
            bst(root.right)
            
            return result
        
        
        bst(root)
        return result[k - 1]