"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        res = []
        
        def binary_search(x, low, high):
            
            if low > high:
                return -1
            
            mid = low + (high-low)//2
            
            temp_result = customfunction.f(x, mid)
            
            if temp_result > z:
                binary_search(x, low, mid-1)
            elif temp_result < z:
                binary_search(x, mid + 1, high)
            else:
                res.append([x, mid])
        
        x  = 1
        y = 1000
        for i in range(1, 1000):
            binary_search(i, x, y)
            
        return res
        