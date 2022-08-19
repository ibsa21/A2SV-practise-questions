class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        inbound = lambda row, col: 0<=row<m and 0<=col<n
        memo = {}
        def dfs(row:int, col:int, moves:int):
            
            if moves > maxMove: return 0
            if not inbound(row, col): return 1
            if (row, col, moves) in memo: return memo[(row, col, moves)]
            
            result = 0       
            for i, j in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                new_row, new_col = row + i, col + j
                result +=dfs(new_row, new_col, moves + 1)

            if not (row, col, moves) in memo:
                memo[(row, col,moves)] = result
            else:
                memo[(row, col, moves)] += result

            return memo[(row, col, moves)]
                
        return dfs(startRow, startColumn, 0)  % (10**9 + 7)
            
            