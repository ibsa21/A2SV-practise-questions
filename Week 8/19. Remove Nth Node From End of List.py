# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_p = head
        fast_p = head
        
        count = 0
        while count < n:
            fast_p  = fast_p.next
            count += 1
        
        # if the nth node is the first node of linked list
        if fast_p == None:
            return head.next
        
        while fast_p.next:
            fast_p = fast_p.next
            slow_p = slow_p.next
        
        slow_p.next = slow_p.next.next
        
        return head
