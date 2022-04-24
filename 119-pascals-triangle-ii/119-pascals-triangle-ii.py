class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        result = [1, 1]
        
        for i in range(2, rowIndex + 1):
            
            mid_result = result[::]
            mid_result.append(1)
            
            k = 0
            for j in range(1, len(mid_result) -1):
                
                mid_result[j] = result[k] + result[k + 1]
                k += 1
            result = mid_result 
        
        return result