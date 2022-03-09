# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        res = []
        q = collections.deque()
        
        q.append(root)
        
        while q:
            q_len = len(q)
            
            level_nodes = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                if not node:
                    level_nodes.append("null")
            
            if level_nodes:
                left = 0
                right = len(level_nodes) -1
                
                while left <= right:
                    if level_nodes[left] != level_nodes[right]:
                        return False
                    left += 1
                    right -= 1
        return True