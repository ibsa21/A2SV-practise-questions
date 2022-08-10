# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if node is None: return

        if node.val > key:
            node.left = self.deleteNode(node.left, key)
        elif node.val < key:
            node.right = self.deleteNode(node.right, key)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None or node.right is None:
                node = node.right if node.right else node.left
            else:
                min_left_value = self.find_min_value(node.right)
                node.val = min_left_value.val
                node.right = self.deleteNode(node.right, min_left_value.val)
        return node
                
    def find_min_value(self, node):
        while node.left is not None:
            node = node.left
        return node
        