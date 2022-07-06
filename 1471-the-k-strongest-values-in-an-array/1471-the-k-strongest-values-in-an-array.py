import functools
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        def custom_sort(num1:int, num2:int)->int:
            nonlocal median
            if abs(median-num1) > abs(median-num2): return 1
            elif abs(median-num1) < abs(median-num2): return -1
            else: 
                if num1 > num2: return 1
                else: return -1
        
        arr.sort()
        median = arr[(len(arr)-1)//2]
        arr = sorted(arr, key = functools.cmp_to_key(custom_sort))[::-1]
        return arr[:k]
    