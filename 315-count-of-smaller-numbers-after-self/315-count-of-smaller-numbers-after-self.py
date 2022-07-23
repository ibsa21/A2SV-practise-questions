class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        result  = [0] * len(nums)
        sorted_nums = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            idx = bisect_left(sorted_nums, nums[i])
            sorted_nums.insert(idx, nums[i])
            result[i] = idx
        return result