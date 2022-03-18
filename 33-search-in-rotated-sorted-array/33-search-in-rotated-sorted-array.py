class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
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
        
        def binary_search(low, high):
            
            if low > high:
                return -1
            mid =  low + (high - low)//2

            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                return binary_search(low, mid-1)
            else:
                return binary_search(mid + 1, high)
        
        if pivot_index == -1:
            return binary_search(0, len(nums)-1)
        else:
            if nums[0] <= target:
                return binary_search(0, pivot_index -1)
            elif nums[-1] >= target or nums[pivot_index]==target:
                return binary_search(pivot_index, len(nums)-1)
            else:
                return -1