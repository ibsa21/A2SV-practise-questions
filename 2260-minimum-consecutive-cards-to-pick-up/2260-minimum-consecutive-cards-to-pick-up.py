class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        numIndex = {}
        
        ans = len(cards)
        found = False
        for i, num in enumerate(cards):
            if num in numIndex:
                 ans = min(ans, i - numIndex[num] + 1)
                 found = True
            numIndex[num] = i
        
        if not found:return -1
        return ans
            