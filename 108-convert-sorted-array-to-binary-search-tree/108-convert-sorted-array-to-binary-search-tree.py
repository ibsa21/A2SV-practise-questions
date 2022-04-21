# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        mid_index = len(nums)//2
        
        bst = TreeNode(nums[mid_index])
        
        bst.left = self.sortedArrayToBST(nums[:mid_index])
        bst.right = self.sortedArrayToBST(nums[mid_index + 1:])
        
        return bst
            
            
        