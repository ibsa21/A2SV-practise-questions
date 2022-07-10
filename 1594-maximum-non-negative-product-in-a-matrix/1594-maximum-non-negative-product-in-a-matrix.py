class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid),len(grid[0])
        
        dp = [[(1,1) for i in range(col_len)] for j in range(row_len)]
        dp[0][0] = (grid[0][0], grid[0][0])

        for i in range(row_len):
            for j in range(col_len):
                if i==0 and j==0:continue
                
                if i==0 or j==0:
                    values = dp[max(0, i-1)][max(0, j-1)]
                else:
                    values = dp[i][j-1] + dp[i-1][j]
                    
                dp[i][j] = (min(values) * grid[i][j], max(values) * grid[i][j])
        
        res = max(dp[-1][-1])
        return -1 if res < 0 else res %(10**9+7)