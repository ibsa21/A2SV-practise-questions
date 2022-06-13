class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_falling_sum = float(inf)
        
        m, n = len(matrix), len(matrix[0])
        inbound = lambda x, y: 0<=x < m and 0 <= y< n
        
        dp = {}
        def dfs(row, col):
            if inbound(row, col):
                
                if (row, col) in dp:
                    return dp[(row, col)]
                
                if row == m-1:
                    return matrix[row][col]
                
                middle = dfs(row + 1, col)
                right = dfs(row + 1, col + 1)
                left = dfs(row + 1, col -1)
                
                dp[(row, col)]  = min([left, right, middle]) + matrix[row][col]
                return dp[(row, col)]
                
            else:
                return float(inf)
                
        
        for start_col in range(m):
            min_falling_sum = min(min_falling_sum, dfs(0, start_col))
        
        return min_falling_sum