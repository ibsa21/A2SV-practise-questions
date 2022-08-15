# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head):
        if head is None or head.next is None: return head
        nextNode = head.next
        newNode = self.reverseList(nextNode)
        nextNode.next = head
        head.next = None
        return newNode
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        linkedList = []
        kthList, last = None, None
        count = 0
        while head:
            count += 1
            node = ListNode(head.val)
            if kthList is None:
                kthList = node
                last = node
            else:
                last.next = node
                last = node
            
            if count == k:
                linkedList.append(kthList)
                kthList, last = None, None
                count = 0
            head =head.next
    
        head, last = None, None
        for node in linkedList:
            curList = self.reverseList(node)
            if not head:head = curList
            else:last.next = curList
                
            last = curList
            while curList.next:
                last = curList.next
                curList = curList.next
        if kthList:
            last.next = kthList
        return head