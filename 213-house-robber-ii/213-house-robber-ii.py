class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i, nums, memo):
            
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i + 2, nums, memo) + nums[i], dfs(i + 1, nums, memo))

            return memo[i]

        return max(nums[0], dfs(0, nums[:-1], {}), dfs(0, nums[1:], {}))