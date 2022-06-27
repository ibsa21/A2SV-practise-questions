# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        root.val = 0
        q = deque()                         # type: Deque
        q.append(root)
        max_width = 1                       # type: int
        
        while q:
            q_len = len(q)                  # type: int
            count_left_right = 0
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    if node.left: 
                        node.left.val = (2 * node.val) + 1
                        q.append(node.left)
                    if node.right: 
                        node.right.val = (2 * node.val) + 2
                        q.append(node.right)
                        
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)                  # type: int
            count_left_right = 0
            start, end = None, None
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    if not start: start = node.val
                    end = node.val
                    q.append(node.left)
                    q.append(node.right)
            if start and end: max_width = max(max_width, end - start + 1)
        return max_width