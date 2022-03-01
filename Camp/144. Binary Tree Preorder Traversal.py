# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_seq = []
        
        def traverse(root):
            if not root:
                return

            
            preorder_seq.append(root.val)
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        return preorder_seq
