class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.total_sum = sum(nums)
        count = 0
        memo = {}
        def recursive(i:int, curr_sum:int):
            if i >= len(nums):
                if curr_sum == target:return 1
                else: return 0
                
            if (i, curr_sum) in memo: return memo[(i, curr_sum)]
            memo[(i, curr_sum )] = (recursive(i+1, curr_sum + nums[i]) \
                                     + recursive(i+1, curr_sum - nums[i]))
            return memo[(i, curr_sum)]
            
        return recursive(0, 0)
        return count