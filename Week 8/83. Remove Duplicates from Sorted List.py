# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_pointer = head
        return_head = None
        newHead = None
        
        while (curr_pointer):
            if (return_head==None):
                return_head = ListNode(curr_pointer.val)
                newHead = return_head
                
            elif return_head.val != curr_pointer.val:
                return_head.next = ListNode(curr_pointer.val)
                return_head = return_head.next
            else:
                curr_pointer = curr_pointer.next
                
        return newHead
            
            
            
