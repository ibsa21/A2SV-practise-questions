class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = set()
        
        def backtrack(i, current):
            
            if i >= len(nums):
                if len(current) >= 2:
                    ans.add(tuple(current))
                
            if len(current) >= 2:
                ans.add(tuple(current))
            
            for idx in range(i, len(nums)):
                    
                if len(current) == 0 or current[-1] <= nums[idx]:
                    backtrack(idx+1, current + [nums[idx]])
        
        backtrack(0, [])
        return ans