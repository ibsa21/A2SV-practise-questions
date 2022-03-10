# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.sum_nodes = 0
        
        def dfs(root, parent, grandParent):
            
            if not root:
                return
            
            if grandParent and grandParent.val % 2 ==0:
                self.sum_nodes += root.val
            
            if root.left:
                dfs(root.left, root, parent)
                
            if root.right:
                dfs(root.right, root, parent)
        
        dfs(root, None, None)
        
        return self.sum_nodes
            
            
            