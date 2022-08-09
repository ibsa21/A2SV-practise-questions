class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        def backtrack(nums, path, result):
            if not nums:
                result.append(path)
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i]==nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], result)
        result = list()
        backtrack(nums, [], result)
        return result