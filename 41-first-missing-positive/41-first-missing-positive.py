class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = Counter(nums)
        max_number = max(nums)
        if max_number < 1:return 1
        for i in range(1, max_number + 2):
            if  i not in hashset :return i