class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row_len , col_len = map(len,(grid,grid[0])) 
        q = deque()

        one_count = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    one_count += 1
        
        def isValid(new_row, new_col, grid):
            return  0 <= new_row < row_len and 0<=new_col< col_len and grid[new_row][new_col] == 1

        neighbours =[(1,0),(-1,0),(0,1),(0,-1)]
        minutes_taken = 0
        while q:
            q_len = len(q)
            is_changed = False
            for _ in range(q_len):

                row ,col = q.popleft()
                
                for r , c in neighbours:
                    new_row = row + r
                    new_col =  col + c

                    if isValid(new_row, new_col, grid):
                        q.append((new_row,new_col))
                        grid[new_row][new_col] = 2
                        is_changed =True
                        one_count -= 1


            if is_changed:
                minutes_taken +=1
        
        if one_count != 0:
            return -1
        
        return minutes_taken