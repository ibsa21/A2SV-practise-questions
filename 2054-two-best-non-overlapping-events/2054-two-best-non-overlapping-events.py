class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        #step - 1: sort the events based on starting time of events
        events.sort()
        

        curr_time_max, global_max_time = 0, 0
        heap = []
        
        for curr_interval in events:
            
            while heap:
                max_end_time, time_value = heappop(heap)
                
                if max_end_time >= curr_interval[0]:
                    heappush(heap, (max_end_time, time_value))
                    break
                
                curr_time_max = max(curr_time_max, time_value)
            
            global_max_time = max(global_max_time, curr_time_max + curr_interval[2])
            heappush(heap, (curr_interval[1], curr_interval[2]))
        
        return global_max_time
                