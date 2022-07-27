# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        """
        self.prev_node = None
        
        def preorder_traversal(node):
            if not node: return 
            
            preorder_traversal(node.right)
            preorder_traversal(node.left)
            
            
            node.right = self.prev_node
            node.left = None
            self.prev_node = node
        preorder_traversal(root)
        