class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        #define prefix sum
        prefix_sum = [nums[0]] * len(nums)
        for i, num in enumerate(nums):
            if i==0:continue
            prefix_sum[i] = prefix_sum[i-1] + num
        
        number_valid_splits = 0
        for i in range(len(nums)-1):
            first_split = prefix_sum[i]
            second_split = prefix_sum[-1]-first_split
            if first_split >= second_split: number_valid_splits += 1
        return number_valid_splits