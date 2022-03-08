"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root and len(root.children)==0:
            return 1
        if not root:
            return 0
        
        queue = deque()
        queue.append((root.children, 1))
        max_depth = 0
        
        while queue:
            
            r, depth_t = queue.popleft()
            depth_t += 1
            max_depth = max(max_depth, depth_t)
            for i in range(len(r)):
                if r[i].children:
                    queue.append((r[i].children, depth_t))
        return max_depth
                