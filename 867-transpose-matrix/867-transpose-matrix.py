class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose  = [[None] * len(matrix) for  i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for idx, num in enumerate(matrix[i]):
                transpose[idx][i] = num
        return transpose