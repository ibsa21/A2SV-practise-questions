class Solution:
    def fib(self, n: int) -> int:
    
        #bottom  up approach + tabulation
        dp = [0] * n
        
        for i in range(n):
            if i <=1:
                dp[i]=1
            else:
                dp[i] = dp[i-1] + dp[i -2]
                
        return dp[-1] if dp else 0
    
        #top-down approach
        
        def recursive(n, memo):
            if n < 2:
                return 1
            
            if n in memo:
                return memo[n]
            else:
                memo[n] = recursive(n-1) + recursive(n-2)
                return memo[n]
        
        return recursive(n, {})