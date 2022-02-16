# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        #convert linked list to an array
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
            
            
        #create monotonic stack
        list_stack = []
        
        #create result array
        result = [0] * len(head_list)
        
        for i in range(len(head_list)):
            
            while list_stack and head_list[i] > head_list[list_stack[-1]]:
                result[list_stack.pop()] = head_list[i]
            
            list_stack.append(i)
            
        return result
        
