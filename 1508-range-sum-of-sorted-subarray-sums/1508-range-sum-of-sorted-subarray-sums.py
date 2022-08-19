class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        subArraySum = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subArraySum.append(sum(nums[i:j + 1]))
                
        subArraySum.sort()
        sum_value = 0
        for i in range(left-1, right):
            sum_value += subArraySum[i]
            
        return sum_value % (10**9 + 7)