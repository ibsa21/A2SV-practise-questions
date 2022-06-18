class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sum_value = 0
        left_sum = 0
        total_sum = sum(nums)
        
        for i in range(len(nums)):
            
            if left_sum == total_sum - (left_sum + nums[i]):
                return i
            left_sum+=nums[i]
        return -1