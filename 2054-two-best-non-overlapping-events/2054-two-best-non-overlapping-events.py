class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        #step - 1: sort the events based on starting time of events
        events.sort()
        
        curr_interval_max, global_max_time = 0, 0
        
        #step -2: store the end_time and value of intervals
        heap = []
        
        # step-3: for each intervals find a event that starts before it and calculate the max_time
        for curr_interval in events:
            
            while heap:
                
                if heap[0][0] < curr_interval[0]:
                    curr_interval_max = max(curr_interval_max, heappop(heap)[1])
                else:
                    break
            
            global_max_time = max(global_max_time, curr_interval_max + curr_interval[2])
            heappush(heap, (curr_interval[1], curr_interval[2]))
        
        return global_max_time
                