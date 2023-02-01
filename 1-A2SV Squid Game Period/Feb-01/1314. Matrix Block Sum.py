class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix_sum = [[0] for _ in range(len(mat))]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                prefix_sum[row].append(prefix_sum[row][-1] + mat[row][col])

        
        answer = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                start_row = max(0, row -k)
                end_row = min(len(mat)-1, row + k)
                start_col = max(0, col -k)
                end_col = min(len(mat[0])-1, col + k)

                current_total_sum = 0
                for r in range(start_row, end_row+1):
                    current_total_sum += prefix_sum[r][end_col+1] - prefix_sum[r][start_col]
                answer[row][col] = current_total_sum
        return answer
