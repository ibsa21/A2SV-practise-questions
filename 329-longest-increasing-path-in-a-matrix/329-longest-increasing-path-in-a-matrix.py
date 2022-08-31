class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROW_LEN, COL_LEN = len(matrix), len(matrix[0])
        
        getMatValue = lambda x, y: matrix[x][y]
        inbound = lambda row, col: 0<=row < ROW_LEN and 0<= col < COL_LEN
        Point  = Tuple[int, int]
        
        memo = {}
        def dfs(currPoint:Point, prevValue:int)->int:
            
            if not inbound(*currPoint) or getMatValue(*currPoint) <= prevValue:
                return 0
            
            if currPoint in memo: return memo[currPoint]
            
            result  = 1
            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newPoint = (currPoint[0]  + i, currPoint[1] + j)
                # if newPoint not in memo:
                result = max(result, dfs((newPoint), getMatValue(*currPoint)) + 1)
                
            memo[currPoint] = result if not currPoint in memo else max(result, memo[currPoint])
            return memo[currPoint]     
        
# {(0, 0): 1, (0, 2): 1, (0, 1): 2, (0, 3): 2}
        ans = 1
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                if (row, col) not in memo:
                    ans = max(ans, dfs((row, col), -1))
        return ans