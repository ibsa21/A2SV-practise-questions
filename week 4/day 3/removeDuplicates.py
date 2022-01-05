class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        j = 0
        for i in set(nums):
            if j==0:
                nums[j] = nums[0]
            else:
                index += nums.count(nums[j-1])
                nums[j], nums[index] = nums[index], nums[j]
            j +=1
        return len(set(nums))
