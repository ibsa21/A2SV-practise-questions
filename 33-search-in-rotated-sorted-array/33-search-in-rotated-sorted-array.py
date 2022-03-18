class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
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
        
        pivot_index = -1
        
        for i in range(len(nums)):
            if i < len(nums) -1 and  nums[i] > nums[i+1]:
                pivot_index = i + 1
                break
        
        if pivot_index == -1:
            return binary_search(0, len(nums)-1)
        else:
            if nums[0] <= target:
                return binary_search(0, pivot_index -1)
            elif nums[-1] >= target or nums[pivot_index]==target:
                return binary_search(pivot_index, len(nums)-1)
            else:
                return -1