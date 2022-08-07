# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(node, ref_head):
            if node is None: return False
            if ref_head.val != node.val: return False
            ref_head = ref_head.next
            if ref_head is None: return True
            if dfs(node.left, ref_head)==True or dfs(node.right, ref_head)==True:
                return True
            return False
        def head_finder(node):
            if node is None: return False
            if node.val == head.val:
                ref_head = head
                if dfs(node, ref_head) == True: return True
            
            if head_finder(node.left) or head_finder(node.right): return True
            return False
        
        return head_finder(root)