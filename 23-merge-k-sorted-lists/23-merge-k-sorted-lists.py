# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        all_list = []
        
        if not lists:
            return 
        
        for i in range(len(lists)):
            
            list_a = lists[i]
            
            while list_a:
                all_list.append(list_a.val)
                list_a = list_a.next
            
        ref_head = None
        last = None
        all_list.sort()
        
        for i in range(len(all_list)):
            
            temp = ListNode(all_list[i])
            if not ref_head:
                ref_head = temp
                last = temp
            else:
                last.next = temp
                last = temp
        return ref_head