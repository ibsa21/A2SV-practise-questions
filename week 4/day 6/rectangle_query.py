class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:   
        for i in range(row1, row2+1):
            x = self.rectangle[i]
            self.rectangle[i] = x[:col1] + [newValue] * (abs(col2 - col1) + 1) + x[col2+1:]
        
    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
                
        

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
