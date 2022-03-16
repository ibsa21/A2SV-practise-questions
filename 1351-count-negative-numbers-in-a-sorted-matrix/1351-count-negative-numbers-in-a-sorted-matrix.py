class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        visited = set()
        count_negative = 0
        
        def isValid(r, c):
            return (0<= r < len(grid) and 0<=c<len(grid[0])) and ((r,c) not in visited and grid[r][c] < 0)
        
        def dfs(row, col):
            
            nonlocal count_negative
            for i, j in directions:
                new_row = row + i
                new_col = col + j
                
                if isValid(new_row, new_col):
                    visited.add((new_row, new_col))
                    count_negative += 1
                    dfs(new_row, new_col)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] < 0 and (i, j) not in visited:
                    count_negative +=1
                    visited.add((i,j))
                    dfs(i, j)
                    
                    
        return count_negative