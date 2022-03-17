# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        inorder_traversal = []
        
        #traverse inorder 
        def dfs(root):
            
            nonlocal bst_stack
            if not root:
                return 
            
            
            dfs(root.left)
            inorder_traversal.append(root.val)
            dfs(root.right)
            
        dfs(root)
        
        bst_stack = inorder_traversal[:]
        bst_stack.sort()
        
        incorrect = []
        
        #find the incorrect node
        for i in range(len(inorder_traversal)):
            if inorder_traversal[i] != bst_stack[i]:
                incorrect.append(inorder_traversal[i])
                
        # recover the binary search tree
        def insert_correct(root):
            if not root:
                return 
            
            if root.val == incorrect[1]:
                root.val = incorrect[0]
            elif root.val == incorrect[0]:
                root.val = incorrect[1]
            
            insert_correct(root.left)
            insert_correct(root.right)
            
        insert_correct(root)
                