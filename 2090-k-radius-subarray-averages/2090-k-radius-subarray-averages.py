class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        invalid = lambda i: i - k  >=0 and i + k < len(nums)
        
        for i, num in enumerate(nums):
            if i !=0 :
                nums[i] += nums[i-1]        
        ans = []
        for i in range(len(nums)):
            l, r = i - k - 1, i + k
            if not invalid(i):
                ans.append(-1)
            else:
                left, right = nums[l], nums[r]
                if l < 0:
                    left = 0
                ans.append(int(math.floor(right - left)//(2 * k  + 1)))
        return ans