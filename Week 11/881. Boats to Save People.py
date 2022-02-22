class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort(reverse=True)
        #[50, 49, 47, 41, 33, 26, 22, 18, 13, 12, 11, 10, 10, 10, 7, 6, 6, 2, 2, 2]

        
        left  = 0
        right = len(nums)-1
        result = 0
        
        while left <= right:
            sum_value = nums[left]
            if sum_value + nums[right] <= limit:
                sum_value += nums[right]
                right -=1
            
            left += 1
            
            result += 1
        return result
            
            
            
        
