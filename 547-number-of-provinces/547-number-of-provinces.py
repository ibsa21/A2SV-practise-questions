class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row, col = map(len, (isConnected, isConnected[0]))
        
        adjecancy_list = {}
        
        for i in range(row):
            adjecancy_list[i] = []
            for j in range(col):
                if isConnected[i][j] == 1 and i !=j:
                    adjecancy_list[i].append(j)
        
        visited = set()
        
        def dfs(node):
            visited.add(node)    
            for n in adjecancy_list[node]:
                if n not in visited:
                    dfs(n)
        
        res = 0
        for i in range(row):
            if i not in visited:
                res += 1
                dfs(i)
        return res
                