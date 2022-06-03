class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sum = [[0] * len(matrix[0]) for  i in range(len(matrix))]
        
        for i in range(len(self.matrix)):
            self.prefix_sum[i][0] = self.matrix[i][0]
            for j in range(1, len(self.matrix[i])):
                self.prefix_sum[i][j]= self.prefix_sum[i][j-1] + self.matrix[i][j]
        print(self.prefix_sum)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1, row2 + 1):
            result += (self.prefix_sum[i][col2] - self.prefix_sum[i][col1] + self.matrix[i][col1])
        return result
                

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)