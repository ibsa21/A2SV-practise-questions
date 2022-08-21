import math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n==0: return len(tasks)
        
        tasks_sorted_bf = [(value, key) for key, value in Counter(tasks).items()]
        tasks_sorted_bf.sort(reverse =True)
        
        number_units = 0
        for idx, (value, task) in enumerate(tasks_sorted_bf):
            last_position = ((n + 1) * (value-1)) + (idx + 1)
            number_units = max(last_position, number_units)
            
        return max(len(tasks), number_units)        
        
        