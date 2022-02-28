# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False
        elif root2.val != root1.val:
            return False
        
        return self.isSameTree(root1.right, root2.right) and self.isSameTree(root1.left, root2.left)
