class Solution:
    def minDeletions(self, s: str) -> int:
        freq = list(Counter(s).values())
        freq.sort(reverse = True)
        seen_before = set()
        deleted_count = 0
        for num in freq:
            while num > 0 and  num in seen_before:
                deleted_count += 1
                num -= 1
            seen_before.add(num)
        return deleted_count