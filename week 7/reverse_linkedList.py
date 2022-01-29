# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reversed_node(head)[0]
    
    def reversed_node(self, node):
        if node == None or node.next==None:
            return (node, node)
        
        head, reversed_node = self.reversed_node(node.next)
        reversed_node.next = node
        node.next = None
        return  (head, node)
        
        
        
        
        
        
                
        
            
        
        
