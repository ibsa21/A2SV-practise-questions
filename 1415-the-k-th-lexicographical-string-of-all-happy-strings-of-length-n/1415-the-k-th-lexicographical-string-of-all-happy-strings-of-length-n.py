class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        path = {'a':('b', 'c'), 'b':('a', 'c'), 'c':('a', 'b')}
        letters = ['a', 'b', 'c']
        visited = set()
        result = []
        
        def dfs(node, string):
            if string in visited: return
            if len(string)==n:
                result.append(string)
                visited.add(string)
                return
            for char in path[node]:
                dfs(char, string + char)
        
        for key in path:
            dfs(key, key)
        
        return '' if len(result) < k else result[k-1]