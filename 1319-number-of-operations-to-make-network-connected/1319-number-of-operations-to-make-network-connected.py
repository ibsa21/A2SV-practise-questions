class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        visited = set()
        graph = defaultdict(list)
        self.edge_counter = 0

        for start, end in connections:
            graph[start].append(end)
            graph[end].append(start)

        def dfs(node):
            
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    self.edge_counter += len(graph[neigh])
                    dfs(neigh)
                
        
        components = 0
        free_cables = 0
        prev = 0
        for key in range(n):
            if key not in visited:
                visited.add(key)
                self.edge_counter = len(graph[key])
                dfs(key)
                free_cables += self.edge_counter//2 - (len(visited)-prev)+1
                self.edge_counter = 0
                components += 1
                prev = len(visited)
        if free_cables >= components-1:
            return components-1 
        return -1