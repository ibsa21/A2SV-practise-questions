class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        memo = {}
        def dfs(idx, cur_sum):
            if cur_sum==0: return True
            if idx >= len(nums) or cur_sum < 0: return False
            
            if (idx, cur_sum) in memo: return memo[(idx, cur_sum)]
            
            memo[(idx, cur_sum)] = dfs(idx + 1, cur_sum) or dfs(idx + 1, cur_sum - nums[idx])
            return memo[(idx, cur_sum)]
            
        total_sum = sum(nums)
        if total_sum %2==1: return False
        return dfs(0, total_sum//2)
            
        