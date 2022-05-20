class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n, m, result = len(grid)-1, len(grid[0])-1, 0
        
        memo = {}
        def dp(i, j):
            nonlocal result
            if i >  n or j > m or grid[i][j]==1:return 0
            
            if (i, j) in memo:return memo[(i, j)]
            if i == n and j==m:return 1
            
            memo[(i, j)] = dp(i + 1, j) + dp(i, j + 1)
            return memo[(i,j)]
        return dp(0, 0)
            