class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def find_totalTrips(duration):
            
            total_trip = 0
            for i in range(len(time)):
                total_trip += math.floor(duration/time[i])
            return total_trip
        
        low = 1
        high = max(time) * totalTrips
        min_duration  = high
        
        def binary_search(low, high):
            nonlocal min_duration
            
            if low > high:
                return
            
            mid = low + (high - low)//2
            total_trips = find_totalTrips(mid)
            
            if total_trips >= totalTrips:
                min_duration = min(min_duration, mid)
                binary_search(low, mid -1)
            else:
                binary_search(mid + 1, high)
                
        binary_search(low, high)
        return min_duration