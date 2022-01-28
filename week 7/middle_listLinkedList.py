# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #first-approach
        counter = 0
        current = ListNode()
        current = head
        while(head):
            counter += 1
            head = head.next
        
        counter = counter //2
        i = 0
        while(i < counter):
            current  = current.next
            i +=1
        
        return current
    
    #second approach
        slowPointer  = head
        fastPointer = head
        
        while(fastPointer and  fastPointer.next):
            fastPointer = fastPointer.next.next;
                
            slowPointer = slowPointer.next;
        
        return slowPointer
