class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for val in nums:
            
            if val < 0:
                val  *= -1
                
            nums[val-1] = - abs(nums[val-1])
        print(ans, nums)
        
        for index, val in enumerate(nums):
            if val > 0:
                ans.append(index+1)
        
        return ans