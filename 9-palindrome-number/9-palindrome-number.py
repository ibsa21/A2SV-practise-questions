class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        left  = 0
        right = len(x) -1 
        
        while left <= right:
            if x[right] != x[left]:
                return False
            left += 1
            right -= 1
        return True