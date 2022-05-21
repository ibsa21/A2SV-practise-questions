class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        for num in set(nums):
            if count[num] > len(nums)/3:result.append(num)
        return result