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
        visitedA = set()
        visitedB = set()
        ref = headA
        
        while headA or headB:
            # print(headA in visitedB, headB in visitedA, visitedA)
            if headA in visitedB:return headA
            if headB in visitedA:return headB
            
            if headB:
                visitedB.add(headB)
                headB = headB.next
            if headA:
                visitedA.add(headA)
                headA = headA.next
                
        while ref:
            if ref in visitedB:return ref
            
            ref = ref.next
        return None
        # for nodes in visitedA:
        #     if nodes in visitedB: return nodes
        # return None