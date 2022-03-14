class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here

        # if graph is not connected
        if n-len(edges) > 1:
            return False

        #create adjecancy_list
        adjecancy_list = {}

        for i in range(n):
            adjecancy_list[i] = []
        
        for j in range(len(edges)):
            adjecancy_list[edges[j][0]].append(edges[j][1])
            adjecancy_list[edges[j][1]].append(edges[j][0])
        
        visited = set()
        cycle = False
        
        def dfs(node, parent):

            visited.add(node)

            for vertex in adjecancy_list[node]:
                if vertex != parent and vertex in visited:
                    cycle = True
                    return 
                if vertex  not in visited:
                    dfs(vertex, node)
        
        dfs(0, -1)

        if len(visited) != len(edges) + 1 or cycle:
            return False
        return True
