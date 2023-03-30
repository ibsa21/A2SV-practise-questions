class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        n = 2**n
        answer = []
        
        for val in range(0, n):
            bin_str = bin(val)[2:].zfill(len(nums))
            local_subset = []
            for index, bi_digit in enumerate(bin_str):   
                if bi_digit == '1':
                    local_subset.append(nums[index])
            answer.append(local_subset)
        
        return answer