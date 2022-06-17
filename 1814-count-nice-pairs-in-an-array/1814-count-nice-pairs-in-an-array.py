class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            rev = int(str(num)[::-1])
            nums[idx] = num - rev
        counter = Counter(nums)
        num_good_pairs = 0
        for key in counter:
            num_good_pairs += (counter[key] * (counter[key]-1))//2
        
        return (num_good_pairs % (pow(10, 9) + 7))