class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def largest(a, b):
            if a + b < b+a:
                return 1
            else:
                return 0
            
        nums = list(map(str, nums))
        
        for x in range(len(nums)-1, -1, -1):
            for y in range(x):
                if largest(nums[y], nums[y+1]):
                    nums[y], nums[y+1] = nums[y+1], nums[y]

        return str(int("".join(nums)))
                
        
