class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        best = 0
        def binary_search(left, right, arr):
            nonlocal best
            
            if left > right:
                return
            
            mid = left + (right-left)//2
            
            if arr[mid] < 0:
                best += right-mid + 1
                binary_search(left, mid-1, arr)
            else:
                binary_search(mid + 1, right, arr)
        
        result = 0
        
        for arr in grid:
           binary_search(0, len(arr)-1, arr)
        
        return best
            