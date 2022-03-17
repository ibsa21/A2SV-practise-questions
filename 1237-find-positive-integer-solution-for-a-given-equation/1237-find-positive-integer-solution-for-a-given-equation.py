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
        for i in range(1,1000):

            left, right = 1, 1000
            while left <= right:

                mid  = left + (right - left)//2
                temp = customfunction.f(i, mid)
                if temp == z:
                    res.append([i, mid])
                    break
                elif temp > z:
                    right = mid - 1
                elif temp < z:
                    left = mid + 1
        return res