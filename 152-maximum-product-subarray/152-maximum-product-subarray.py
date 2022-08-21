class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1
        
        for num in nums:
            if num == 0:
                curr_min, curr_max = (1, 1)
                continue
            
            temp = curr_max * num
            curr_max = max(num * curr_min, num *curr_max, num)
            curr_min = min(num * curr_min,  temp, num)
            
            res = max(curr_max, res)
            print(res, curr_max, curr_min)
        return res