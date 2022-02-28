# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:            
        return self.calculate(root, 0, targetSum)
    
    
    def calculate(self, root, sum_value, target):
            if not root:
                return False

            sum_value += root.val
            
            if not root.left and not root.right:
                if sum_value == target:
                    return True
                else:
                    return False
            
            left = self.calculate(root.left, sum_value, target)
            right = self.calculate(root.right, sum_value, target)

            return left or right
