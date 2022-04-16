class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                
        
    
        #dynamic programming approach
        buy_stock, max_profit = float(inf), 0
        
        for i in range(len(prices)):
            buy_stock = min(prices[i], buy_stock)
            max_profit = max(max_profit, abs(prices[i] - buy_stock))
        
        return max_profit
