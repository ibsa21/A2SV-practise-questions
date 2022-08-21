class Solution:
    # can we use n-days
    def isPossible(self, bloomDay:List[int], waiting_days:int, expectedBouquets:int, k:int)->bool:
        
        adjecant = 0
        for num_days in bloomDay:
            adjecant = adjecant + 1 if num_days <= waiting_days else 0
            if adjecant == k:
                expectedBouquets -= 1
                adjecant = 0
        return expectedBouquets <=0
        
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m * k > len(bloomDay): return -1
        
        smallest_waiting_day, highest_waiting_day = 1, max(bloomDay)
        while smallest_waiting_day < highest_waiting_day:
            mid_waiting_day = smallest_waiting_day + (highest_waiting_day - smallest_waiting_day)//2
            
            if self.isPossible(bloomDay, mid_waiting_day, m, k):
                highest_waiting_day = mid_waiting_day
            else:
                smallest_waiting_day = mid_waiting_day + 1
        return smallest_waiting_day