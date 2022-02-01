class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
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
    
            """
        Approaches taken to solve the problem:
                step1. Sort the numbers - sorting takes O(nlogn)
                step2. use slide window technique - the size of the window is  ( right-left + 1 ) 
                step3. nums[right']  * (right-left + 1) > total_sum + k
                    Explanation: in every iteration we consider the number at the right index to be the target number
                                 nums[right] - represents the target number
                                 if target number multplied by window size is greater than (current total sum + k), 
                                 the current window size does not give us the result we wanted so we have to decrease the window size from left
        """
        
        
