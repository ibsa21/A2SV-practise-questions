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
        self.next_node = None
        
        def preorder_traversal(node):
            if not node: return 
            
            right = preorder_traversal(node.right)
            left = preorder_traversal(node.left)
            
            node.right = self.next_node
            node.left = None
            self.next_node = node
            
        preorder_traversal(root)
        