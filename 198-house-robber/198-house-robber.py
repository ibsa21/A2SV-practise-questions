class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        memo = {}
        
        def dfs(i, robbing):
            
            if i >= len(nums):
                return 0
            
            if (i,robbing)  in memo:
                return memo[(i, robbing)]
            
            memo[(i, robbing)] = max(dfs(i  + 2, robbing) + nums[i], dfs(i + 1, robbing))
            
            return memo[(i, robbing)]
        
        return dfs(0, True)