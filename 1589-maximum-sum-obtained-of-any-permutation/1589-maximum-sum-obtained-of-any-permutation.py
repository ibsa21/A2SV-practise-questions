from bisect import bisect_left
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        counter = [0] * len(nums)
        for start, end in requests:
            counter[start] += 1
            if end + 1 < len(nums):
                counter[end + 1] -= 1
            
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        
        counter.sort()
        nums.sort()
        
        ans, right  = 0, len(nums)-1
        while right > -1 and counter[right] != 0:
            ans += (counter[right] * nums[right])
            right -= 1
        return ans % ((10**9) + 7)