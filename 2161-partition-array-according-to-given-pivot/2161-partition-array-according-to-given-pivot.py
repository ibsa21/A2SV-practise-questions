class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        lessthan = []
        greaterthan  = []
        equal_pivot = []
        
        for num in nums:
            if num < pivot:
                lessthan.append(num)
                
            elif num > pivot:
                greaterthan.append(num)
            else:
                
                equal_pivot.append(num)
        
        lessthan.extend(equal_pivot)
        lessthan.extend(greaterthan)
        
        return lessthan
