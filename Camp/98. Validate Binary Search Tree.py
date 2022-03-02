# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        
        
        traversed = []
        
        
        def traverse(root):
            
            if not root:
                return
            
            traverse(root.left)
            traversed.append(root.val)
            traverse(root.right)
        
            return traversed
        
        traversed = traverse(root)
        
        for i in range(1, len(traversed)):
            
            if traversed[i] <= traversed[i-1]:
                return False
        return True
