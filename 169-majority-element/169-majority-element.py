class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        result = (nums[0], count[nums[0]])
        for key in count:
            if count[key] > result[1]:
                result = (key, count[key])
        
        return result[0]