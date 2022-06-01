# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_p = head
        slow_p = head
        
        cycle_found = False
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            
            if fast_p == slow_p:
                cycle_found = True
                break
        
        if not cycle_found: return None
        
        pointer = head
        while pointer != fast_p:
            pointer = pointer.next
            fast_p = fast_p.next
        
        return pointer