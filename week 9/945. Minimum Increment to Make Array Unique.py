class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums or len(nums)==1:
            return 0
        
        result = 0
        nums.sort()
        
        left = 0
        max_number = nums[0] 
        for i in range(1, len(nums)):
            
            rightEl = nums[i]
            if rightEl <= max_number:
                result += max_number - nums[i] + 1
                rightEl = max_number + 1
                
            max_number = rightEl
        return result
                
    
    
    
