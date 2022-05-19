class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        pivot_index = -1
        
        def search_range(low, high, k_target):
            nonlocal pivot_index
            
            if low > high:
                return
            
            mid = low + (high-low)//2
            if k_target < nums[mid]:
                search_range(mid + 1, high, k_target)
            elif k_target > nums[mid]:
                pivot_index = mid
                search_range(low, mid-1, k_target)
                
        search_range(1, len(nums)-1, nums[0])
        return nums[0] if pivot_index == -1 else nums[pivot_index]