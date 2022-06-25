class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        #increasing from left to right
        increasing_nums = nums[:]
        left_count  = 0
        for idx, num in enumerate(increasing_nums):
            if idx == 0:continue
            if num < increasing_nums[idx-1]:
                increasing_nums[idx] = increasing_nums[idx-1]
                left_count += 1
        if left_count <= 1: return True
        
        #decreasing from right to left
        right_count = 0
        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] > nums[idx + 1]:
                nums[idx] = nums[idx + 1]
                right_count += 1
        if right_count <=1: return True
        return False