class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # if target is less than current capacity
        if target <= startFuel: return 0
            
        dp = [startFuel] + [0] * len(stations)        
        for i, (curr_distance, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= curr_distance:
                    dp[j +1] = max(dp[j + 1], dp[j] + fuel)

        for idx, max_reach in enumerate(dp):
            if max_reach >= target: return idx
        return -1
