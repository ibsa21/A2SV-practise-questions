# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        #if not root:
         #   return TreeNode(val)
        
        def helper(root,value):
            if not root:
                return TreeNode(value)
            elif value<root.val:
                root.left = helper(root.left,value)
            elif value>root.val:
                root.right = helper(root.right,value)
                
            return root
        
        return helper(root, val)
        