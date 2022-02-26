#approach 1 swapping values only
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ref_head = None
        
        while head and head.next:
            
            head.val, head.next.val = head.next.val, head.val
            
            if not ref_head:
                ref_head = head
            head  = head.next.next
        return ref_head
