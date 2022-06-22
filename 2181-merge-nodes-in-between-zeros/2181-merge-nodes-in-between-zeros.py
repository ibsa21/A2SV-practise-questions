# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_node = None
        last = None
        head = head.next
        sum_between_nodes = 0
        
        while head:
            if head.val == 0:
                temp_node = ListNode(sum_between_nodes)
                sum_between_nodes = 0
                if not result_node:
                    result_node = temp_node
                    last = temp_node
                else:
                    last.next = temp_node
                    last = temp_node
            sum_between_nodes += head.val
            head = head.next
        
        return result_node