# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        
        deepest_nodes = []
        while q:
            q_len = len(q)
            level_nodes = []
            for _ in range(q_len):
                node = q.popleft()
                
                if node:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level_nodes:
                deepest_nodes = level_nodes
        
        return sum(deepest_nodes)
                    
                
                