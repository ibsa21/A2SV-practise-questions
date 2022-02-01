class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Approaches taken to solve the problem:
                step1. Sort the numbers - sorting takes O(nlogn)
                step2. use slide window technique - the size of the window is right-left + 1
                
        """
        
        
        nums.sort()
        left = 0
        right = 0
        
        total_sum = 0
        maxFreq  = 0
        
        while right < len(nums):
            
            total_sum += nums[right]
            
            while nums[right] * (right - left + 1) > total_sum + k:
                total_sum -= nums[left]
                left += 1
            
            maxFreq = max(maxFreq, (right-left + 1))
            right  += 1
            
        return maxFreq
        
