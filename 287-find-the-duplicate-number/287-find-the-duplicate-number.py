class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        slow_pointer  = 0
        fast_pointer  = 0
        for i in range(len(nums)):
            
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            
            if slow_pointer == fast_pointer:
                break
            
        
        slow_pointer = 0
        
        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]
        
        return fast_pointer
        
        
            