class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = defaultdict(int)
        for idx, num in enumerate(nums):
            rev[num] = int(str(num)[::-1])
            nums[idx] = num - rev[num]
        counter = Counter(nums)
        num_good_pairs = 0
        for key in counter:
            num_good_pairs += (counter[key] * (counter[key]-1))//2
        
        return (num_good_pairs % (pow(10, 9) + 7))