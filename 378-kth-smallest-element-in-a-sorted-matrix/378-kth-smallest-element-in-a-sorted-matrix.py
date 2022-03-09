class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        flatten_list = []
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                flatten_list.append(matrix[i][j])
        
        flatten_list.sort()
        
        return flatten_list[k-1]