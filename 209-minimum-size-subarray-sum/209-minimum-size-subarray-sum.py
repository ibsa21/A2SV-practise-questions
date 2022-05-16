class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left, right, ans = 0, 0, len(nums) + 1
        
        cur_sum = 0
        while right <= len(nums)-1:
            cur_sum += nums[right]
            while left < len(nums) and cur_sum >= target:
                ans = min(ans, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                
            right += 1
        return ans if ans != len(nums) + 1 else 0