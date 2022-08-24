from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]

        memo = {}
        def dp(i):
            if i in memo: return memo[i]
            
            if i > 365:
                return 0
            else:
                result = float("inf")
                if i in dayset:
                    result = min(dp(i + d) + c for c, d in zip(costs, durations))
                else:
                    result = dp(i + 1)
                
                memo[i] = result
                return memo[i]
        return dp(1)