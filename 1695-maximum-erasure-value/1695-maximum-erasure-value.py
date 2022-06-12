class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        ans = 0
        l,r = 0,0
        
        stack = set()
        curr_sum = 0
        while r < len(nums):
            is_found = False
            
            curr_sum += nums[r]
            if nums[r] in stack:is_found = True
            while stack and nums[r] in stack and nums[l] != nums[r]:
                stack.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            
            if is_found:
                stack.remove(nums[r])
                curr_sum -= nums[r]
                l += 1
                
            stack.add(nums[r])
            ans = max(curr_sum, ans)
            r += 1
        return ans
            
                