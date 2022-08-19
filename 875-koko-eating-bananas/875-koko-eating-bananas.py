import math
class Solution:
    
    def getTotalHours(self, piles:List[int], k:int)->int:
        total_hours  = 0
        for num_bananas in piles:
            total_hours += math.ceil(num_bananas/k)
        return total_hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)
        
        while low <= high:
            mid = low + (high - low)//2
            
            if self.getTotalHours(piles, mid) <= h:
                smallest_k = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return smallest_k
    
    