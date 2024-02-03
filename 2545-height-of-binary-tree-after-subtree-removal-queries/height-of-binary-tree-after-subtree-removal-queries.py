# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        subtree_height = {}
        tree_height_after_removal = {}
        cousins = defaultdict(list) # keep the size of the cousins at level just 2
        
        def traversal(node, depth):
            if not node:
                return 0
            
            left = traversal(node.left, depth + 1)
            right = traversal(node.right, depth + 1)
            subtree_height[node.val] = max(left, right) + 1
            
            height = max(left, right) + 1
            
            if len(cousins[depth]) == 2 and cousins[depth][0][0] < height:
                heappop(cousins[depth])
            
            if len(cousins[depth])!=2:
                heappush(cousins[depth], (height, node.val))
            
            return subtree_height[node.val]

        traversal(root, 1)
        
        def dfs_traversal(node, depth):
            if not node:
                return
            
            max_height = depth - 1
            for height, cousin in cousins[depth]:
                if cousin != node.val:
                    max_height = max(max_height, depth + height -1)
                    
            tree_height_after_removal[node.val] = max_height
            
            dfs_traversal(node.left, depth + 1)
            dfs_traversal(node.right, depth + 1)
        
        dfs_traversal(root, 1)
        answer = []
        
        for query in queries:
            answer.append(tree_height_after_removal[query] - 1)
        
        return answer