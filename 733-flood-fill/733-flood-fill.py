class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        neighbors = [(1,0), (0, -1), (-1,0), (0, 1)]
        row_len, col_len = map(len, (image, image[0]))
        
        val = image[sr][sc]
        
        visited = set()
        
        def dfs(row, col):
            
            visited.add((row, col))
            
            image[row][col] = newColor
            
            for r, c in neighbors:
                
                new_row, new_col = row + r, col + c
                
                if (0 <= new_row  < row_len) and (0 <= new_col  < col_len):
                    
                    if image[new_row][new_col]==val and (new_row, new_col) not in visited:
                        dfs(new_row, new_col)
        dfs(sr, sc)
        return image
                
            