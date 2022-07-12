class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Time complexity: O(row_len * col_len)
        Space complexity: O(row_len * col_len)
        """
        row_len, col_len  = len(board), len(board[0])
        neighbors_life = [[(0, 0) for col in range(col_len)] for row in range(row_len)]
        
        inbound = lambda row, col: 0<= row < row_len and 0<= col < col_len
        directions = [(-1, 0), (1, 0), (0,1), (1, 1), (-1, -1), (-1, 1), (0,-1), (1, -1)]
        
        # determine number of live and dead neighbors for each cell
        for row in range(row_len):
            for col in range(col_len):
                alive, dead = 0, 0
                for r, c in directions:
                    if inbound(row + r, col + c):
                        if board[row + r][col + c] == 1: alive += 1
                        else: dead += 1
                neighbors_life[row][col] = (alive, dead)
        
        # apply the rules
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == 1:
                    if neighbors_life[row][col][0] < 2 \
                    or neighbors_life[row][col][0] > 3: 
                        board[row][col] = 0
                else:
                    if neighbors_life[row][col][0] == 3: board[row][col] = 1
                    

                            