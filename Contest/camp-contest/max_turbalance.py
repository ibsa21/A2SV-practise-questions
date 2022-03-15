class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        def compareNumbers(x, y):
            
            sign_magnitude = 0
            if x < y:
                sign_magnitude = -1
            elif x > y:
                sign_magnitude = 1
            return sign_magnitude
        
        left = 0
        result = 1
        
        for i in range(1, len(arr)):
            
            sign = compareNumbers(arr[i-1], arr[i])
            
            is_changed = False
            if sign ==0:
                is_changed = True
                
            elif i <= len(arr)-2 and  sign * compareNumbers(arr[i], arr[i+1]) != -1:
                result = max(result, i - left + 1)
                is_changed = True
                
            elif i==len(arr)-1:
                result = max(result, i - left + 1)
                is_changed = True
                
            if is_changed:
                left = i
        return result
