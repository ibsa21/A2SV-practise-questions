class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        max_weight = max(weights)
        total_weight = sum(weights)
        min_capacity = total_weight
        
        def find_numberDays(weight):
            
            no_days = 0
            
            i = 0
            while i < len(weights):
                
                sum_weight = 0
                
                is_changed = False
                while i < len(weights) and  sum_weight + weights[i] <= weight:
                    sum_weight += weights[i]
                    i += 1
                    is_changed = True
                    
                if not is_changed:
                    i += 1
                no_days += 1
            
            if no_days <= days:
                return True
            else:
                return False
        
        def binary_search(low, high):
            
            nonlocal min_capacity
            
            if low > high:
                return 
            mid = low + (high-low)//2
            
            if find_numberDays(mid):
                min_capacity = min(min_capacity, mid)
                binary_search(low, mid-1)
            else:
                binary_search(mid + 1, high)
            
        binary_search(max_weight, total_weight)    
        return min_capacity