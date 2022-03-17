# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root, depth):
            
            if not root:
                return (root, depth-1)
            
            depth += 1
            left = dfs(root.left, depth)
            right = dfs(root.right, depth)

            
            if left[1]==right[1]:
                return (root, left[1])
            
            elif left[1] > right[1]:
                
                return left
            else:
                return right
        
        return dfs(root, 0)[0]
        
                
            
            