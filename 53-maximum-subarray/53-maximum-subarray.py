class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        table = [0] * len(nums)
        table[-1] = nums[-1]
        max_result = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            
            table[i] = max(table[i + 1] + nums[i], nums[i])
            max_result = max(table[i], max_result)
        
        print(table)
        return max_result
            