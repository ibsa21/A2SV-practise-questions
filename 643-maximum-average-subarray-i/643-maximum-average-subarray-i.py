class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right, ans, cur_sum = 0, 0, -float(inf), 0
        while right < len(nums):
            cur_sum += nums[right]
            if right - left + 1==k:
                ans  = max(cur_sum/k, ans)
                cur_sum   -= nums[left] 
                left +=1
            right += 1
        return ans