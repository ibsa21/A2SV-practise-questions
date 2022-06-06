# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visitedB = set()
        
        while headB:
            
            visitedB.add(headB)
            headB = headB.next
            
        while headA:
            if headA in visitedB:return headA
            
            headA = headA.next
        return None
        # for nodes in visitedA:
        #     if nodes in visitedB: return nodes
        # return None