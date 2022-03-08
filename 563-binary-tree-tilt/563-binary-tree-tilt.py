# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.tilt_sum = 0
        def dfs(root):
            #print(root.val)
            if not root:
                return 0
            
            if not root.left and not root.right:
                return root.val
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.tilt_sum += abs(left-right)
            return left + right + root.val
        dfs(root)
        return self.tilt_sum