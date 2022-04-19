class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        left = 0
        i = 0
        
        while i < len(nums):
            
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
        
            i += 1
        
        return left
        
#         last_index = len(nums) -1
#         left = 0
#         while left < len(nums) and left < last_index:
            
            
#             if nums[left] == val and left != last_index:
                
#                 while last_index > -1 and nums[last_index] == val:
#                     last_index -= 1
                    
#                 nums[left], nums[last_index] = nums[last_index], nums[left]
            
#             left += 1
#         return left if last_index >= 0 else 0