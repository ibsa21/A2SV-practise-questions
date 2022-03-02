# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.stack = []
        def smallest(root):
            
            if not root:
                return
            
            smallest(root.left)
            self.stack.append(root.val)
            smallest(root.right)
            
            return self.stack
        return smallest(root)[k-1]
