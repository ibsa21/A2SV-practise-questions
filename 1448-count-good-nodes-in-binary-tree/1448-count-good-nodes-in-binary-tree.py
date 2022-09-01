# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        ans = 0
        def dfs(node, maxNode):
            nonlocal ans
            if not node: return
            
            if node.val >= maxNode:
                ans += 1
            
            dfs(node.left, max(maxNode, node.val))
            dfs(node.right, max(maxNode, node.val))
            
        dfs(root, root.val)
        return ans
        