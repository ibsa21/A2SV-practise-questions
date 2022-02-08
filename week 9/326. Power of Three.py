class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        return self.power_recursive(n)
    
    def power_recursive(self,n):
        if n==1:
            return True
            
        if n < 3:
            return False
        return self.power_recursive(n/3)
