# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nums   = []
        while head:
            nums.append(head.val)
            head = head.next
        
        last = 0
        new_array = []
        for i in range(len(nums)):
            if nums[i] < x:
                new_array.insert(last, nums[i])
                last += 1
            else:new_array.append(nums[i])
        
        head, last = None, None
        for num in new_array:
            temp_node = ListNode(num)
            if not head:
                head  = temp_node
                last = temp_node
            else:
                last.next  = temp_node
                last = temp_node
        
        return head