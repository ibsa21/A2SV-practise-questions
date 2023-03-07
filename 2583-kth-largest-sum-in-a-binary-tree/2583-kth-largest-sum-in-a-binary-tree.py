# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        
        levels = []
        
        q = deque([root])
        while q:
            
            _sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                
                if node:
                    _sum += node.val
                    q.append(node.left)
                    q.append(node.right)
            
            levels.append(_sum)
            
        levels.sort()
        return levels[len(levels)-k] if k < len(levels) else -1
                