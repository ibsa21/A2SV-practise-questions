# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head  = None
        return_head  = None
        
        while l1 and l2:
            newNode = None
            num1 = l1.val
            num2 = l2.val
            if num1 <= num2:
                newNode = ListNode(num1)
                l1 = l1.next
            else:
                newNode = ListNode(num2)
                l2 = l2.next
            
            if not head:
                head = newNode
                return_head = head
            else:
                head.next = newNode
                head  = newNode
        
        if not head:
            if l1:
                return_head = l1
            if l2:
                return_head = l2
                
        if l1 and head:
            head.next = l1
            
        if l2 and head:
            head.next = l2
        
        return return_head
        # MergeSort in Python
