class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        answer = 0
        for key, value in counter.items():
            if key != 0:
                answer += 1
        return answer