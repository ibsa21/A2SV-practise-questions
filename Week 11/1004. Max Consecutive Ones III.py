class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        
        left = 0
        right = 0
        ans = 0
        
        while right < len(nums):
            
            # decrement k by 1
            if nums[right]==0:
                k -= 1
            
            # if k is less than zero slide your window from left
            while k < 0:
                print(k)
                if nums[left]==0:
                    k +=1
                left += 1
                
            
            ans = max(ans, right-left + 1)
            right += 1
        return ans
        
