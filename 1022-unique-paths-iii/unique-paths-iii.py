class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        starting = None
        non_obstacle_count = 0
        answer = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    starting = [row,col]
                if grid[row][col] == 0:
                    non_obstacle_count += 1
        
        def isValid(row,col,m,n):
            if not (0<=row<m and 0<=col<n):
                return False
            
            return grid[row][col] != -1
        
        
        def backtrack(row, col, path):
            nonlocal  non_obstacle_count, answer
            
            # print(path, len(path), non_obstacle_count, (row,col))
            if grid[row][col] == 2:
                if len(path) - 1 == non_obstacle_count:
                    # print(path, len(path), non_obstacle_count)
                    answer += 1
                return
            
            path.add((row, col))
            
            for x,y in direction:
                new_row = row + x
                new_col = col + y
                
                if isValid(new_row, new_col, m,n) and (new_row, new_col) not in path:
                    backtrack(new_row, new_col, path)
                    
            path.remove((row,col))
            return answer
        
        return backtrack(starting[0], starting[1], set())