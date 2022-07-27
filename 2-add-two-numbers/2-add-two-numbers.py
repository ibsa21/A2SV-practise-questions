# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumReturn= None
        last = None
        carrier = 0
        
        while(l1 or l2):
            
            num1 = l1.val if l1 !=None else 0
            num2 = l2.val if l2 !=None else 0
            
            sumValue = num1 + num2 + carrier
            if (sumValue > 9):
                sumValue = sumValue % 10
                carrier = 1
            else:
                carrier = 0
                
            result = ListNode(sumValue)
            
            if sumReturn == None:
                sumReturn = result
                last = result
            else:
                last.next = result
                last = result
            
            if l1:
                l1 = l1.next
            if l2 :
                l2 = l2.next
                
        if carrier > 0:
            carrierNode = ListNode(carrier)
            last.next = carrierNode
            last = carrierNode
        return sumReturn 