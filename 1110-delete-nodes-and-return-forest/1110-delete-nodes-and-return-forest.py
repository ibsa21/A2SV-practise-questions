# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        set_to_delete = set(to_delete)
        list_roots = []
        def dfs(node, parent, is_left):
            if not node: return
            dfs(node.left, node, True)
            dfs(node.right, node, False)
            if node.val in set_to_delete:
                if parent != None and is_left:parent.left = None
                elif parent != None:parent.right = None
                if node.left and node.left.val not in set_to_delete:
                    list_roots.append(node.left)
                if node.right and node.right.val not in set_to_delete:
                    list_roots.append(node.right)
        dfs(root, None, False)
        if root.val not in set_to_delete: list_roots.append(root)
        return list_roots