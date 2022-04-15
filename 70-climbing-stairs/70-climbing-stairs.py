class Solution:
    def climbStairs(self, n: int) -> int:
        
        last_step = 1
        prev_last_step = 1
        
        result = 1
        for i in range(n-2, -1, -1):
            result = last_step + prev_last_step
            last_step = prev_last_step
            prev_last_step = result
        
        return result