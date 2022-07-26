# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        adj_list = defaultdict(set)
        leaves  = set()
        count = 0
        def dfs_find_matrix(node, parent):
            nonlocal count
            if not node: return
            node.val = count
            count += 1
            if not node.right and not node.left:
                leaves.add(node.val)
            if parent:
                adj_list[node.val].add(parent.val)
                adj_list[parent.val].add(node.val)
            dfs_find_matrix(node.left, node)
            dfs_find_matrix(node.right, node)
        dfs_find_matrix(root, None)
        
        number_good_pairs = 0
        visited = set()
        counted_pair = set()
        
        print(adj_list, leaves)
        def dfs(node, curr_distance, curr_leaf):
            nonlocal number_good_pairs
            if curr_distance > distance: return
            
            if node in leaves and node != curr_leaf \
                and ((curr_leaf, node) not in counted_pair and (node, curr_leaf) not in counted_pair): 
                number_good_pairs += 1
                counted_pair.add((curr_leaf, node))
                return
            visited.add(node)
            for next_node in adj_list[node]:
                if next_node not in visited:
                    dfs(next_node, curr_distance +1, curr_leaf)
                    
        for leaf in leaves:
            dfs(leaf, 0, leaf)
            visited = set([leaf])
        return number_good_pairs    