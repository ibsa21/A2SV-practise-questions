# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        def dfs(node, path):
            nonlocal res            
            if not node:return
            path.append(node.val)

            if not node.left and not node.right:
                res.append(path.copy())
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
            
        dfs(root, [])
        
        for i in range(len(res)):
            res[i] = '->'.join(map(str, res[i]))
        return res