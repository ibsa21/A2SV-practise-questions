class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        path = {'a':('b', 'c'), 'b':('a', 'c'), 'c':('a', 'b')}
        letters = ['a', 'b', 'c']
        visited = set()
        result = set()
        def dfs(node, string):
            if len(string)==n:
                result.add(string)
                return
            
            for char in path[node]:
                dfs(char, string + char)
        
        for key in path:
            dfs(key, '')
        result = list(result)
        result.sort()
        return '' if len(result) < k else result[k-1]