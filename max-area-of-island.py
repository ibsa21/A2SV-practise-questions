class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        max_area = 0

        def isValid(row, col):
            if not (0<=row<len(grid) and 0<=col<len(grid[0])):
                return False
            if (row,col) in visited:
                return False
            if grid[row][col] == 0:
                return False
            return True

        def dfs(row, col):

            if not isValid(row, col):
                return
                
            visited.add((row,col))
            for x,y in directions:
                new_row = row + x
                new_col = col + y
                dfs(new_row, new_col)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                prev_length = len(visited)
                dfs(row,col)
                max_area = max(max_area, len(visited)-prev_length)

        return max_area