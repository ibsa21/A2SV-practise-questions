class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        q = deque([[0, [0]]])
        result = []
        while q:
            node, path = q.popleft()
            if node == len(graph)-1:
                result.append(path)
                
            for nextNode in graph[node]:
                q.append([nextNode, path + [nextNode]])
        return result
        
        