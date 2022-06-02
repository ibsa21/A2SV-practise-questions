class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        return list(zip(*matrix))
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]       

#         return matrix
#         transpose  = [[None] * len(matrix) for  i in range(len(matrix[0]))]
#         for i in range(len(matrix)):
#             for idx, num in enumerate(matrix[i]):
#                 transpose[idx][i] = num
#         return transpose