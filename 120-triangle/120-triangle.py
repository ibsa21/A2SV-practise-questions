class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        #bottom-up + tabulation approach
        row_len = len(triangle)
        table = triangle[-1]
        
        for r in range(row_len-2, -1, -1):
            col_len  = len(triangle[r])
            col_table = [0] *  col_len
            for c in range(col_len -1, -1, -1):
                col_table[c] = triangle[r][c] + min(table[c], table[c + 1])
            table = col_table
        return table[0]
    
    #top-down + memoization approach
        memo = {}
        
        def dfs(i,j):
            if i == len(triangle):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = triangle[i][j] + min(dfs(i+1,j) , dfs(i+1,j+1))
            return memo[(i,j)]
        
        return dfs(0,0)