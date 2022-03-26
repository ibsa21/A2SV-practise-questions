class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: 
        sorted_arr = [0] * len(nums)
        
        left = 0
        right = len(nums)-1
        
        index = len(sorted_arr) -1 
        
        while left <= right:
            
            if abs(nums[left]) >= abs(nums[right]):
                
                sorted_arr[index] = nums[left] * nums[left]
                
                left += 1
            else:
                sorted_arr[index] = nums[right] * nums[right]
                right -= 1
            
            index -= 1
        
        return sorted_arr
        
        
                
            