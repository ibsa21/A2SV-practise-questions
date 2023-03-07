# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.prev = root.val
        self.count = 0
        self.max_count = [0, None]
        self.answer = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            
            # print(root.val, self.prev, self.max_count, self.count)
            if root.val != self.prev:
                if self.count > self.max_count[0]:
                    self.answer = [self.prev]
                    self.max_count = [self.count, self.prev]
                elif self.count == self.max_count[0]:
                    self.answer.append(self.prev)
                self.count = 0
                
            self.prev = root.val    
            self.count += 1       
            # print(self.answer)
            
            inorder(root.right)
        inorder(root)
        if self.count > self.max_count[0]:
            self.answer = [self.prev]
        elif self.count == self.max_count[0]:
            self.answer.append(self.prev)
        return self.answer