from itertools import combinations
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        maximum_length = 0
        for r in range(1, len(arr) + 1):
            for comb in combinations(arr, r):
                length_char = sum(len(substring) for substring in comb)
                if len(set(''.join(comb))) == length_char:
                    maximum_length = max(maximum_length, length_char)
        return maximum_length