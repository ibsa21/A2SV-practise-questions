class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe_node = {}
        
        
        
        def dfs(i):
            
            if i in safe_node:
                return safe_node[i]
            
            safe_node[i]  = False
            
            for neighbor in graph[i]:
                
                if not dfs(neighbor):
                    return False
            
            safe_node[i] = True
            return True
            
            
        result = []
        for i in range(len(graph)):
            
            if dfs(i):
                result.append(i)
        
        return result