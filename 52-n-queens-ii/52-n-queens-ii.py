class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        """
        Backtracking problem
        Note: All the quens must be in different row and different col
        """
        
        isValidPos = lambda a, b, c: a not in set_cols and b not in rightleftdiag and c not in leftrightdiag
        
        set_cols  = set()
        rightleftdiag = set()
        leftrightdiag = set()
        
        chessboard = [['.'] * n for i in range(n)]
        ans = 0
        
        def backtrack(row):
            nonlocal ans
            if row == n:
                ans += 1
                return
            
            for cols in range(n):
                if isValidPos(cols, row + cols, row - cols):
                    set_cols.add(cols)
                    rightleftdiag.add(row+cols)
                    leftrightdiag.add(row - cols)
                    
                    backtrack(row + 1)
                
                    #backtrack
                    set_cols.remove(cols)
                    rightleftdiag.remove(row+cols)
                    leftrightdiag.remove(row - cols)    
        
        backtrack(0)
        return ans