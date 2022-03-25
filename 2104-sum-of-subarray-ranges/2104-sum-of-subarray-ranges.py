class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        sum_total = 0
        for i in range(len(nums)):
            
            max_arr = nums[i]
            min_arr = nums[i]
            
            for j in range(i, len(nums)):
                
                if nums[j] < min_arr:
                    min_arr = nums[j]
                
                if nums[j] > max_arr:
                    max_arr = nums[j]
                sum_total += (max_arr - min_arr)
                
        return sum_total
        
        