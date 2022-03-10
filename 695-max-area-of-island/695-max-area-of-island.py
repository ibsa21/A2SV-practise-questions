class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = map(len, (grid, grid[0]))
        directions = [(-1,0), (1, 0), (0, 1), (0, -1)]
        
        visited = set()
        queue = collections.deque()
        self.max_area = 0
        
        def isValid(r, c):
            return (0 <= r < row_len and 0 <= c < col_len) and ( (r,c) not in visited and grid[r][c] == 1)
        
        def bfs(row, col):
            area_count = 1
            
            while queue:    
                r_row, r_col = queue.popleft()
                
                for r, c in directions:
                    new_r = r_row + r
                    new_c = r_col + c

                    if isValid(new_r, new_c):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        area_count += 1
                                 
            self.max_area = max(self.max_area, area_count)
            
        for i in range(row_len):
            for j in range(col_len):
                if (i, j) not in visited and grid[i][j]==1:
                    visited.add((i, j))
                    queue.append((i, j))
                    bfs(i, j)
                
        return self.max_area