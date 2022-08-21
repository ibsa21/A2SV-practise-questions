import math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n==0: return len(tasks)
        #["A","A","A","B","B","B"], n = 2
        #find the frequency of each task
        
        freq_counter = defaultdict(int)
        for task in tasks:
            freq_counter[task] += 1
        
        #A-3 and B-3
            
        #sorting from the largest to smallest (most frequent to the least frequnt)
        tasks_sorted_bf = [(value, key) for key, value in freq_counter.items()]
        tasks_sorted_bf.sort(reverse =True)
        
        #each time I'do tasks I'll reduce the frequency of the task
        number_units = 0
        for idx, (value, task) in enumerate(tasks_sorted_bf):
            last_position = ((value-1) * (n + 1)) + idx + 1
            number_units = max(last_position, number_units)
            
        return max(len(tasks), number_units)      
        
        