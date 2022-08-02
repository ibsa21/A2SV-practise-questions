import numpy as np
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        # let's start by building the matrix
        def enough(value):
            count = 0
            for i in range(1, m  + 1):
                count += min(value//i, n)
            return count >=k
        
        low, high = 1, m * n
        while low < high:
            mid = low + (high - low)//2
            if not enough(mid):low = mid + 1
            else: high = mid
        
        return low
                       
        
