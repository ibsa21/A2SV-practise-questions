# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        postorder_seq = []
        
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            traverse(root.right)
            postorder_seq.append(root.val)
            
        traverse(root)
        return postorder_seq
