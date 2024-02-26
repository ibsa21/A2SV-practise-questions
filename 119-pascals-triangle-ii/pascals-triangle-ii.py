class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        currentRow = [1]
        previousRow = self.getRow(rowIndex - 1)
        
        for index in range(1, rowIndex):
            currentRow.append(previousRow[index-1] + previousRow[index])
        
        currentRow.append(1)
        
        return currentRow