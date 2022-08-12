class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solve(x, n):
            if n==0: return 1
            
            if n  < 0:
                n  = -n
                x = 1/x
            
            half_result = solve(x, n//2)
            if n % 2==0:
                return half_result * half_result
            else:
                return x * (half_result * half_result)
        return solve(x, n)
            