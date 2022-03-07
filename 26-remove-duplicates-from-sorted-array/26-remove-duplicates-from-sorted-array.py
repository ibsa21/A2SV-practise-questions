class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 0
        right = 0
        
        max_number = max(nums)
        
        while nums[left] != max_number:
            
            if nums[right] > nums[left]:
                nums[left + 1], nums[right]  = nums[right], nums[left + 1]
                left += 1
                
            right += 1
        return left + 1