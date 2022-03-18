class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_index = -1
        
        def find_row(low, high):
            
            while low < high:
                
                mid = low + math.ceil((high - low)/2)

                if matrix[mid][0] == target:
                    return True
                if matrix[mid][0] > target:
                    high = mid -1
                else:
                    low = mid
                
            return high
        
        row = find_row(0, len(matrix)-1)

        if row and type(row) is bool:
            return True
        def binary_search(low, high):
            
            if low > high:
                return
            
            mid = low + (high-low)//2
            print(matrix[row][mid])
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                return binary_search(low, mid-1)
            else:
                return binary_search(mid + 1, high)
            
        return True if binary_search(0, len(matrix[0])-1) else False