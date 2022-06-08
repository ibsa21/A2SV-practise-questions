# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast =head
        behind = None
        while fast and fast.next:
            behind = slow
            slow = slow.next
            fast = fast.next.next
        if not behind:return None
        behind.next = slow.next
        return head
