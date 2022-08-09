class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
            Time complexity: O(N**2)
            Space complexity: O(N)
        '''
        nums.sort()
        max_subset = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_subset = max(max_subset, dp[i])
        
        res = []
        i, prev_num = len(nums)-1, None
        while max_subset != 0:
            if dp[i]==max_subset  and (prev_num is None or prev_num % nums[i] == 0):
                res.append(nums[i])
                prev_num = nums[i]
                max_subset -= 1
            i -= 1
        return res