class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #memoization + dynamic programming
        memo = {}
        
        #decision  - buying/sell: True - buying and False represents selling
        def dfs(i, decision):
            
            if i >= len(prices):
                return 0
            if (i, decision) in memo:
                return memo[(i, decision)]
            
            #if decision is buying a stock
            if decision:
                memo[(i, decision)] = max(dfs(i + 1, not decision) - prices[i], dfs(i + 1, decision))
            else:
                memo[(i, decision)] = max(dfs(i + 2, not decision) + prices[i], dfs(i + 1, decision))
            
            return memo[(i, decision)]
                                          
        return dfs(0, True)
            
            