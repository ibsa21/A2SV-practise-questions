from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [perm for perm in permutations(nums)]
        