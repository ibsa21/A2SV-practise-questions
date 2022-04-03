class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjecancy_list = {}

        for i in range(n):
            adjecancy_list[i] = []
        
        for j in range(len(edges)):
            adjecancy_list[edges[j][0]].append(edges[j][1])
            adjecancy_list[edges[j][1]].append(edges[j][0])
        
        visited_node = set()
        visited_node.add(source)
        def dfs(source):
            
            for node in adjecancy_list[source]:
                if node not in visited_node:
                    visited_node.add(node)
                    dfs(node)
        dfs(source)
        return destination in visited_node