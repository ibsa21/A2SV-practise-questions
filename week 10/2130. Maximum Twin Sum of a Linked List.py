# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Approach 1: converting Linked List to array and using two pointer to find sum 
# time-complexity-> O(n)
# space-complexity->O(n)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        list_head = []
        while head:
            list_head.append(head.val)
            head = head.next
        
        left = 0
        right = len(list_head)-1
        maxSum = 0
        while left < right:
            
            maxSum = max(maxSum, list_head[left] + list_head[right])
            left += 1
            right -= 1
        return maxSum
#Approach 2 : without using extra memory
#time-complexity: O(n)
#space-complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fastPointer = head
        slowPointer = head
        
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            
        secondHalf = self.reverseList(slowPointer)
        
        maxSum = 0
        while secondHalf:
            maxSum = max(maxSum, secondHalf.val + head.val)
            head = head.next
            secondHalf = secondHalf.next
        return maxSum
            
        
        
    def reverseList(self, head: Optional[ListNode] ):
        prev=next_node=None
        
        while head:
            next_node=head.next
            head.next=prev
            prev=head
            head=next_node
            
        return prev
