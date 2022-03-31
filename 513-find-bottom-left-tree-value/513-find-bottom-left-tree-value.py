# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
        
        q = deque()
        q.append(root)
        last_row = [root.val, root.val]
        
        while q:
            q_len = len(q)
            
            level_data = []
            for i in range(q_len):
                node = q.popleft()
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level_data.append(node.val)
            
            if level_data:
                last_row = level_data
        return last_row[0]
            
            