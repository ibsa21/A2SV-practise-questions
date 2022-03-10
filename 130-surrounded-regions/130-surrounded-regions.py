class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        row_len, col_len = map(len, (board, board[0]))
        
        def isValid(r, c):
            return (0 <= r < row_len and 0 <= c < col_len) and ( (r,c) not in visited and board[r][c] == "O")
          
        def dfs(row, col):
            
            for r, c in directions:
                new_r = r + row
                new_c = c + col
                
                if isValid(new_r, new_c):
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c)
        
        for i in range(row_len):
            for j in range(col_len):
                #print((i, j), i in (0, row_len -1), j in (0, col_len -1), (i, j) not in visited,  board[i][j]=="O")
                if (i in (0, row_len -1) or j in (0, col_len -1)) and ((i, j) not in visited and board[i][j]=="O"):
                    visited.add((i,j))
                    dfs(i, j)
        
        print(visited)
        for i in range(row_len):
            for j in range(col_len):
                if (i, j) not in visited and board[i][j]=="O":
                    board[i][j] = "X"
            
                
        