class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        row_len, col_len = len(grid), len(grid[0])
        visited = set()
        original_grid_color = grid[row][col]
        
        def is_valid(row, col):
            return (0 <= row < row_len and 0<=col < col_len) and (row, col) not in visited
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def is_border(row, col):
            nonlocal original_grid_color
            if row == 0 or col==0 or row == row_len -1 or col == col_len-1: return True
            for r, c in directions:
                new_r, new_col  = row + r, col + c
                if is_valid(new_r, new_col) and grid[new_r][new_col] != grid[row][col]: return True
            return False
        
        def dfs(row, col):
            for r, c in directions:
                new_row, new_col = row + r, col + c
                if (new_row, new_col) == (3, 4):
                    print(is_valid(3, 4), is_border(3, 4))
                if is_valid(new_row, new_col) and grid[new_row][new_col] ==original_grid_color:
                    if  is_border(new_row, new_col):grid[new_row][new_col] = color
                    visited.add((new_row, new_col))
                    dfs(new_row, new_col)            
        dfs(row, col)
        if is_border(row, col):grid[row][col] = color
        return grid