class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        inbound = lambda r, c: 0<=r<m and 0<=c<n
        memo  = {}
        def dfs(l, r):
            
            if inbound(l, r):
                if l==m-1 and r==n-1: return 1
                if (l, r) in memo: return memo[(l, r)]
                
                memo[(l, r)] = dfs(l + 1, r) + dfs(l, r + 1)
                return memo[(l, r)]
            else: return 0
        return dfs(0, 0)