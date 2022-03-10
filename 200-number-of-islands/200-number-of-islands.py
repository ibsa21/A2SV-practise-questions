class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row_len, col_len= map(len, (grid, grid[0]))
        directions = [(-1,0), (1, 0), (0, 1), (0, -1)]
        
        queue = collections.deque()
        
        no_islands = 0            
        visited = set()
        
        def isValid(r, c):
            return (0<=r<row_len and 0 <= c < col_len) and (grid[r][c]=="1" and (r, c) not in visited)
    
        #print(queue)
        
        def bfs(row, col):
            
            while queue:

                row, col = queue.popleft()
                for r, c in directions:
                    new_row = row + r
                    new_col =  col + c

                    if isValid(new_row, new_col):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
        
        #iterate over the grid
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j]=="1" and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append((i, j))
                    bfs(i, j)
                    no_islands += 1
                
        return no_islands