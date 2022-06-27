# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before_left, last, count = None, None, 1
        while count < left:
            new_node = ListNode(head.val)
            if not before_left:
                before_left = new_node
                last = new_node
            else:
                last.next = new_node
                last = new_node
            head = head.next
            count += 1
            
        between_left_right, last_between  = None, None
        while count <= right:
            new_node = ListNode(head.val)
            if not between_left_right:
                between_left_right = new_node
                last_between = new_node
            else:
                new_node.next = between_left_right
                between_left_right = new_node
            head = head.next
            count += 1
        if last:last.next  = between_left_right
        else:before_left = between_left_right
        last = last_between
        
        while head:
            new_node = ListNode(head.val)
            last.next = new_node
            last = new_node
            head = head.next
        return before_left
        