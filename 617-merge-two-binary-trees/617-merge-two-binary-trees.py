# Definition for a binary tree node.
# class TreeNode(object)
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
                
        def dfs(merged, root1, root2):
            
            if not root1 and not root2:return
            elif not root1:
                return root2
            elif not root2:
                return root1
            
            merged = TreeNode(root1.val + root2.val)
                        
            merged.left = dfs(merged.left, root1.left, root2.left)
            merged.right = dfs(merged.right, root1.right, root2.right)
            return merged
        # merged = dfs(None, root1, root2)
        return dfs(None, root1, root2)