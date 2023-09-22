# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def traversal(node, path):
            if not node:
                return 0

            if not node.left and not node.right:
                return int(path+str(node.val))
            
            left = traversal(node.left, path+str(node.val))
            right = traversal(node.right, path+str(node.val))
            return left + right
        
        return traversal(root, '')