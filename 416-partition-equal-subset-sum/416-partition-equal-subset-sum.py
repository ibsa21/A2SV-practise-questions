class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # return False
        memo = {}
        def dfs(idx, cur_sum):
            
            if cur_sum == total_sum/2: return True
            if idx >= len(nums): return False
            
            if (idx, cur_sum) in memo: return memo[(idx, cur_sum)]
            
            result = dfs(idx + 1, cur_sum) or dfs(idx + 1, cur_sum + nums[idx])
            memo[(idx, cur_sum)]= result
            return memo[(idx, cur_sum)]
            
        total_sum = sum(nums)
        if total_sum % 2 != 0: return False
        return dfs(0, 0)
