class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        output = set()

        def backtrack(index, sequence):
            if index >= len(nums):
                if len(sequence) >= 2:
                    output.add(tuple(sequence[::]))
                return

            backtrack(index+1, sequence)
            if (sequence and  nums[index] >= sequence[-1]) or not sequence:
                backtrack(index+1, sequence + [nums[index]])
        backtrack(0, [])
        return output