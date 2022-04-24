class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        table  = [[1] * i for i in range(1,numRows + 1)]
        
        for i in range(2, numRows):
            
            k = i
            a = 0
            for j in range(1, len(table[i])-1):
                table[i][j] = table[k-1][a] + table[k-1][a + 1]
                a += 1
        return table