# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        nums.sort()
        sorted_nums = None
        last = None
        
        for num in nums:
            tempNode = ListNode(num)
            if not sorted_nums:
                sorted_nums = tempNode
                last = tempNode
            else:
                last.next = tempNode
                last = tempNode
        return sorted_nums