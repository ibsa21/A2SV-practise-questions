class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        a = 0
        b = 0

        for val in nums:
            
            a = ~ b &(a^val)
            b = ~ a & (b^val)
        
        return a
            