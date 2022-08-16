class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            if n & 1 > 0:
                count += 1
            n >>= 1
        return count