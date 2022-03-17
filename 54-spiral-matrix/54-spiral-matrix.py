class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left_s, right_s =  0, len(matrix[0]) - 1
        top_s,  bottom_s = 0, len(matrix) - 1
        
        result = []
        
        while left_s <= right_s and top_s <= bottom_s:
            
            for i in range(left_s, right_s + 1):
                result.append(matrix[top_s][i])
            top_s += 1
            
            for i in range(top_s, bottom_s + 1):
                result.append(matrix[i][right_s])
            right_s -= 1 
            
            
            if left_s > right_s or top_s > bottom_s:
                break
            
            for i in range(right_s, left_s -1,-1):
                result.append(matrix[bottom_s][i])
            bottom_s -= 1 
            
            for i in range(bottom_s, top_s - 1,-1):
                result.append(matrix[i][left_s])
            left_s+=1
            
        return result