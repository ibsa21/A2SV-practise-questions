import math
class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLeft = [nums[0]]
        minRight = deque()
        minRight.append(nums[-1])
        n = len(nums)-1
        
        for i in range(1, len(nums)):
            maxLeft.append(max(maxLeft[-1], nums[i]))
            minRight.appendleft(min(minRight[0], nums[n - i]))
        
        ans = 0
        for i in range(1, len(nums)-1):
            if maxLeft[i-1] < nums[i] < minRight[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
        return ans