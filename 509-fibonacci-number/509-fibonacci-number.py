class Solution:
    def fib(self, n: int) -> int:
        
        #topdown approach + memoization
        
        def recursive(i, memo):
            if i==0:
                return 0
            if i== 1:
                return i
            
            
            if i not in memo:
                memo[i] = recursive(i-1, memo) + recursive(i-2, memo)

                return memo[i]
            else:
                return memo[i]
            
        return recursive(n, {})
        
        #bottom  up approach + tabulation
        dp = [-1] * n
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i -2]
        
        return dp[n-1]