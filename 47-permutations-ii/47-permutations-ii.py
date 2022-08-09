class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, path, result):
            if not nums:
                result.add(tuple(path))
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], result)
        result = set()
        backtrack(nums, [], result)
        return [list(perm) for perm in result]