# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        #gready + depth first search
        visited = {None}
        
        childVisited = lambda parent: parent.left not in visited or parent.right not in visited
        isNodeRoot = lambda node, parent: not parent and node not in visited 
        
        minimum_camera = 0
        def dfs(node, parent):
            nonlocal minimum_camera
            if not node: return

            dfs(node.left, node)
            dfs(node.right, node)

            if isNodeRoot(node, parent) or childVisited(node):
                minimum_camera += 1
                visited.update([node, parent, node.left])
            
            return minimum_camera
        return dfs(root, None)
