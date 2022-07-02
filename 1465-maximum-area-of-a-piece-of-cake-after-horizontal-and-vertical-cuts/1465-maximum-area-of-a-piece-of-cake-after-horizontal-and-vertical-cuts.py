class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_area = 1
        horizontalCuts.sort()
        verticalCuts.sort()
        max_column = max(0, horizontalCuts[0])
        
        for idx, row in enumerate(horizontalCuts):
            if idx != 0:
                max_column = max(max_column, abs(row - horizontalCuts[idx-1]))
        max_column = max(max_column, abs(h-horizontalCuts[-1]))
        
        max_row = max(0, verticalCuts[0])
        for idx, col in enumerate(verticalCuts):
            if idx != 0:
                max_row = max(max_row, abs(col - verticalCuts[idx-1]))
        max_row = max(max_row, abs(w- verticalCuts[-1]))
        print(max_column, max_row)
        return (max_column * max_row) % (pow(10, 9) + 7)