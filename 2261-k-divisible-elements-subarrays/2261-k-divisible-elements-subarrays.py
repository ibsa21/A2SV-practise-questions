class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        prefix  = [int(num % p==0) for num in nums]
        prefix_sum = sum(prefix)
        ans = set()
        for left in range(len(nums)):
            right = len(nums)-1
            prefix_sum -= (prefix[left-1] if left > 0 else 0) 
            cur_prefix = prefix_sum
            
            while cur_prefix > k:
                cur_prefix -= prefix[right]
                right -= 1
            
            for j in range(left, right + 1):
                ans.add(tuple(nums[left:j+1]))
        
        return len(ans)