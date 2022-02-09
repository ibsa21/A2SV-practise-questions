# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fastPointer  = head
        slowPointer = head
        
        while(fastPointer and fastPointer.next):
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        
        #Now reverse the node after the middle element
        secondStart = None
        while slowPointer:
            if secondStart == None:
                secondStart = ListNode(slowPointer.val)
            else:
                temp = secondStart;
                newNode = ListNode(slowPointer.val)
                newNode.next = temp
                secondStart = newNode
            slowPointer = slowPointer.next
        
        while secondStart:
            if head.val != secondStart.val:
                return False
            secondStart = secondStart.next
            head = head.next
        return True
            
