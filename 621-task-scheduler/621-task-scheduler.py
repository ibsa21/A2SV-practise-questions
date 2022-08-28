class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [-values for values in collections.Counter(tasks).values()]
       
        # maxNumber = max(frequency)
        heapq.heapify(frequency)
        maxNumber = -frequency[0]
        
        final = (maxNumber -1) * (n+1)
        c = 0
        for v in frequency:
            if -v == maxNumber:
                c += 1
                
        return max(final + c,len(tasks))
        #tasks
    
                
        