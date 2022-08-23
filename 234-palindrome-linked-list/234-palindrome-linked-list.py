# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        secondHead = head
        def recursive(node):
            nonlocal secondHead
            if not node: return
            
            if recursive(node.next) is False:return False
            
            if node.val != secondHead.val:
                return False
            secondHead = secondHead.next
            return True
        
        return recursive(head)