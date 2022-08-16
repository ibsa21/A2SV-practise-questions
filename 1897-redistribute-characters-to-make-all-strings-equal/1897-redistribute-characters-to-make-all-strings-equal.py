class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        counter = defaultdict(int)
        for word in words:
            for char in word:
                counter[char] += 1
        for key, value in counter.items():
            if value % len(words) != 0: return False
        return True