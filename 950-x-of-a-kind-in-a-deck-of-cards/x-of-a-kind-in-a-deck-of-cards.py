class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        counts = Counter(deck).values()
        
        min_count = min(counts)
        
        for group in range(2, min_count + 1):
            all_true = True
            for count in counts:
                if count % group != 0:
                    all_true = False
            if all_true:
                return True
        return False