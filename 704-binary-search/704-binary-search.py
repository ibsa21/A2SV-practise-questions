class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        def binary_search(left, right):
            
            if left > right:
                return -1
            
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else:
                return binary_search(mid + 1, right)
        
        return binary_search(left, right)