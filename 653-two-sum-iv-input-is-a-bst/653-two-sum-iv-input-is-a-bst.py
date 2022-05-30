# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def binary_search(root, target):
            if not root:return False
            
            if root.val > target: return binary_search(root.left, target)
            elif root.val < target:return binary_search(root.right, target)
            else:
                return True
            
        def inorder(node):
            
            if not node:return
            if k-node.val != node.val and  binary_search(root, k-node.val) :
                return True
            left = inorder(node.left)
            right  = inorder(node.right)
            if left or right:return True
        return True if inorder(root) else False
