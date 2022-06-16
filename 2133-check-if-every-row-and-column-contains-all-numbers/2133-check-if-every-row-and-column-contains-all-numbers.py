class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        sum_n = (n * (n + 1))//2
        def isValid(rowList):
            counter = Counter(rowList)
            cur_sum =0
            for key in counter:
                if counter[key] > 1:return False
                cur_sum += key
            return cur_sum == sum_n
        
        for i in range(n):
            if not isValid(matrix[i]):return False
            colList = [matrix[col][i] for col in range(n)]
            if not isValid(colList):return False
        return True