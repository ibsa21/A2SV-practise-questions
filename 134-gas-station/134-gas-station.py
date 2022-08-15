class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalCost = sum(gas[i]-cost[i] for i in range(len(gas)))
        if totalCost < 0: return -1
        
        ans, cost_prefix = 0, 0
        for i in range(len(gas)):
            cost_prefix += gas[i]-cost[i]
            if cost_prefix < 0:
                ans = i + 1
                cost_prefix = 0
        return ans
        
            
            
            
            