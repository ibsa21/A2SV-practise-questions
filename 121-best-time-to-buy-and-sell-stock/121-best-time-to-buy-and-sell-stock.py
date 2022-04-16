class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        stack = []
        
        max_profit = 0
        for i in range(len(prices)):
            while stack and prices[i] <= stack[-1]:
                if len(stack) > 1:
                    max_profit = max(max_profit, abs(stack[0] - stack.pop()))
                else:
                    stack.pop()
            stack.append(prices[i])
            max_profit = max(max_profit, abs(prices[i]- stack[0]))
        
        return max_profit