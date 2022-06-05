class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])
        visited = set()
        
        directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
        
        isValidState = lambda r, c: 0<=r<row_len and 0<=c<col_len and (r, c) not in visited
        
        def backtrack(row, col, idx):
            if idx == len(word):return True
            
            if not isValidState(row, col) or board[row][col] != word[idx] :return False
            
            visited.add((row, col))
            
            res = backtrack(row -1, col, idx + 1) or backtrack(row + 1, col, idx + 1) or backtrack(row, col + 1, idx + 1) or backtrack(row, col -1, idx + 1)
            visited.remove((row, col))
            if res:return True
                
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False