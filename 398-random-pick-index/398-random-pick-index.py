class Solution:

    def __init__(self, nums: List[int]):
        self.nums_index = defaultdict(set)
        self.nums_index_copy = defaultdict(set)
        for idx, num in enumerate(nums):
            self.nums_index[num].add(idx)
            self.nums_index_copy[num].add(idx)
        

    def pick(self, target: int) -> int:
        if len(self.nums_index[target]) == 0:
            for idx in self.nums_index_copy[target]:
                self.nums_index[target].add(idx)
        return self.nums_index[target].pop()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)