class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        set_nums = set(nums)
        return target in set_nums