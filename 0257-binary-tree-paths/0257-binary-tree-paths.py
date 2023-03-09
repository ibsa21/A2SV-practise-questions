# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        answer = []
        def fn(root, path):
            if not root:
                return
            
            if not root.left and not root.right:
                path.append(str(root.val))
                answer.append('->'.join(path))
                return
            
            fn(root.left, path+[str(root.val)])
            fn(root.right, path+[str(root.val)])
        
        fn(root, [])
        return answer