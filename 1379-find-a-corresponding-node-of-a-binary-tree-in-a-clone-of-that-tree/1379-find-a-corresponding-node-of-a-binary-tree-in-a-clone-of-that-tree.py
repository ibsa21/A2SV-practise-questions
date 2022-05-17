# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        target_ref = None
        def dfs(node):
            nonlocal target_ref
            if not node:return
            if node.val == target.val:
                target_ref = node
                return node
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(cloned)
        return target_ref