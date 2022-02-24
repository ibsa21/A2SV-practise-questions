class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        #reverse entire array
        self.swap(nums, 0, len(nums)-1)
        
        #swap the first k elements
        self.swap(nums, 0, k-1)
        
        #swap left elements
        self.swap(nums, k, len(nums)-1)
    
    def swap(self, nums, left, right):
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
