# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def binary_search(root):
            if not root:
                return None
            
            if val > root.val:
                return binary_search(root.right)
            elif val < root.val:
                return binary_search(root.left)
            else:
                return root
        
        return binary_search(root)