class Solution:
    def hammingWeight(self, n: int) -> int:
        
        hamming_distance = 0
        while n > 0:
            hamming_distance += 1
            n &= n-1
        return hamming_distance