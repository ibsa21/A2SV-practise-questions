# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first = None
        while head:
            new_node = ListNode(head.val)
            if not first:
                first = new_node
            else:
                new_node.next = first
                first = new_node
            head  = head.next
        return first