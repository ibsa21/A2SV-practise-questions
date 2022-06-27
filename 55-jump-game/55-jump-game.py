class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ Gready Approach
            time complexity: O(n)
            space complexity: O(1)
        """
        longest_reach = nums[0]                                     #type: int
        for idx, jump in enumerate(nums):
            if idx != 0:
                if idx > longest_reach: return False
                longest_reach  = max(longest_reach, idx + jump)
        return True
        
        #memoization TLE
        memo  = {}
        def dp(cur_index):
            if cur_index >= len(nums)-1: return True
            if nums[cur_index]==0:return
            if cur_index in memo: return memo[cur_index]
            
            for next_idx in range(cur_index, cur_index + nums[cur_index]):
                can_jump = dp(next_idx + 1)
                if can_jump:
                    memo[next_idx + 1] = can_jump
                    return True
            memo[cur_index] = False
            return False
        return dp(0)