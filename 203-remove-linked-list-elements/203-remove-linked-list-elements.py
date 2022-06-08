# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newhead = None
        last = None
        pointer = head
        while pointer:
            
            temp_node = ListNode(pointer.val)
            if pointer.val != val:
                if not newhead:
                    newhead = temp_node
                    last = temp_node
                else:
                    last.next = temp_node
                    last  = temp_node
            pointer = pointer.next
        
        return newhead
        