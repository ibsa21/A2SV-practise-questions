# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def recursive(node):
            nonlocal head
            if not node: return
            
            if recursive(node.next) is False:return False
            
            if node.val != head.val:
                return False
            head = head.next
            return True
        
        return recursive(head)