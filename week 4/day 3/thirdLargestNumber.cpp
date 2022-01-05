class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        firstMax = max(nums)
        secondMax = nums[0]
        thirdMax = nums[0]
        
        for i in range(1, len(nums)):
            if (nums[i] >= secondMax and nums[i] < firstMax):
                secondMax = nums[i]
                
        for j in range(1, len(nums)):
            if (nums[j] >= thirdMax and nums[j] < secondMax):
                thirdMax = nums[j]
        
        if(len(set(nums))) < 3:
            return firstMax
        else:
            return thirdMax
