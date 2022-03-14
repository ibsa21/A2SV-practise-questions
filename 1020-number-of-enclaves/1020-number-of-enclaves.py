class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = map(len, (grid, grid[0]))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        visited = set()
        count_one  = 0
        
        #check Validity of new directions
        def isValid(r, c):
            return (0 <= r < row_len and 0 <=c < col_len) and (grid[r][c]==1 and (r, c) not in visited)
        
        def dfs(row, col):
            grid[row][col] = 0
            for r, c in directions:
                new_row = row + r
                new_col = col + c

                if isValid(new_row, new_col):
                    visited.add((new_row, new_col))
                    dfs(new_row, new_col)
                        
        count_two = 0
        for i in range(row_len):
            for j in range(col_len):
                if (i in (0, row_len-1) or j in (0, col_len-1)) and grid[i][j]==1:
                    visited.add((i, j))
                    dfs(i, j)
        
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j]==1:
                    count_one +=1
                    
        return count_one
                    
                    
                    
                    
                    
                