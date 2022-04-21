class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        def binary_search(low, high):
            mid = low + (high - low)//2
            
            result  = mid * mid
            
            if x >= result and (mid + 1) * (mid + 1) > x:
                return mid
            elif result < x:
                return binary_search(mid + 1, high)
            else:
                return binary_search(low, mid -1)
        
        return binary_search(0, x)