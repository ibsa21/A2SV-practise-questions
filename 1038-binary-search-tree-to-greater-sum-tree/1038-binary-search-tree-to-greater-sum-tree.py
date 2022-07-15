# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        sorted_bst = []
        def inorder(node):
            if not node: return
            
            inorder(node.left)
            sorted_bst.append(node.val)
            inorder(node.right)
        inorder(root)
        
        prefix_sum = [num for num in sorted_bst]
        for i in range(1, len(sorted_bst)):
            prefix_sum[i] += prefix_sum[i-1]
        
        def sum_greater_right(target)->int:
            low, high = 0, len(sorted_bst)-1
            while low <= high:
                mid = low + (high - low)//2
                if sorted_bst[mid]==target: return prefix_sum[-1] - prefix_sum[mid-1] if mid > 0 else prefix_sum[-1]
                elif sorted_bst[mid] > target: high = mid-1
                else: low  = mid + 1
        def convert_bst_to_greater_tree(node):
            if not node: return
            
            node.val = sum_greater_right(node.val)
            convert_bst_to_greater_tree(node.left)
            convert_bst_to_greater_tree(node.right)
        convert_bst_to_greater_tree(root)
        return root