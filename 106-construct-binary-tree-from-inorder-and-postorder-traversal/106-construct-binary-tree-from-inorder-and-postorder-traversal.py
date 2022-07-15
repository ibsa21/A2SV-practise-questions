# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        io_indexmap = defaultdict(int)
        for idx, value in enumerate(inorder):
            io_indexmap[value]  = idx
            
        self.post_idx = len(postorder)-1
        def recursive(left, right):
            if left > right: return None
            
            curr_parent = postorder[self.post_idx]
            self.post_idx -= 1
            
            root = TreeNode(curr_parent)
            
            root.right = recursive(io_indexmap[curr_parent] + 1, right)
            root.left = recursive(left, io_indexmap[curr_parent]-1)
            return root
        return recursive(0, len(inorder)-1)
                
            
