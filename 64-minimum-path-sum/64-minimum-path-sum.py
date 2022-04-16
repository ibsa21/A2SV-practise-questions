class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row_len, col_len  = len(grid), len(grid[0])
        
        table = [[float(inf)] * (col_len + 1) for j in range(row_len + 1)]
        table[row_len -1][col_len]  = 0
        
        for r in range(row_len - 1, -1, -1):
            for c in range(col_len -1, -1, -1):
                table[r][c] = grid[r][c] + min(table[r + 1][c], table[r][c + 1])
                
        return table[0][0]