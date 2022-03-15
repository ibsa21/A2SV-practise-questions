# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        number_moves = 0
            
        def dfs(root):
            nonlocal number_moves
            if not root:
                return 0
            
            
            left = dfs(root.left) 
            right = dfs(root.right)
            number_moves += abs(left + right + root.val - 1)
            return left + right + root.val - 1
            
        dfs(root)
        return number_moves
