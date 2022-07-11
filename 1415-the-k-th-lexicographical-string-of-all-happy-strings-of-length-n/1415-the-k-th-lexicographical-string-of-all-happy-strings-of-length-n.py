class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        '''
            time complexity: O(2**n)
            space complexity: O(2**n)
        '''
        path = {'a':('b', 'c'), 'b':('a', 'c'), 'c':('a', 'b')}
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