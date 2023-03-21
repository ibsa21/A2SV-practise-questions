class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        rows  = len(maze)
        cols = len(maze[0])
        
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        inbound = lambda row,col: 0<=row<rows and 0<=col<cols
        
        def move(r,c):
            nextPosition = set()
            for move_x, move_y in dirs:
                row,col = r,c
                while inbound(row,col) and  maze[row][col] != 1:
                    row += move_x
                    col += move_y

                if inbound(row,col) and maze[row][col] != 1:
                    nextPosition.add((row,col))
                nextPosition.add((row-move_x, col-move_y))
            return nextPosition
        
        
        def dfs(row,col):
            
            if [row, col] == destination:
                return True
            
            visited.add((row,col))
            nextPositions = move(row,col)
            for new_row, new_col in nextPositions:
                if (new_row, new_col) not in visited:
                    if dfs(new_row, new_col):
                        return True
            return False
        return dfs(*start)