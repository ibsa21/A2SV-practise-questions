class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        #step - 1: sort the events based on starting time of events
        events.sort()
        
        curr_time_max, global_max_time = 0, 0
        heap = []
        
        for curr_interval in events:
            
            while heap:
                
                if heap[0][0] < curr_interval[0]:
                    curr_time_max = max(curr_time_max, heappop(heap)[1])
                else:
                    break
            
            global_max_time = max(global_max_time, curr_time_max + curr_interval[2])
            heappush(heap, (curr_interval[1], curr_interval[2]))
        
        return global_max_time
                