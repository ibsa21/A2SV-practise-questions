class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        len_piles = len(piles)
        memo  = {}
        def dp(left, right):
            
            if left > right: return 0
            if (left, right) in memo: return memo[(left, right)]
            
            # determine whose turn it's using this formula (right - left - len) % 2
            if (right - left-len_piles) % 2 == 1:
                memo[(left, right)] = max(piles[left] + dp(left + 1, right), \
                                          piles[right] + dp(left, right-1))
                return memo[(left, right)]
            else:
                memo[(left, right)] = min(-piles[left] + dp(left + 1, right), \
                                          -piles[right] + dp(left, right-1))
                return memo[(left, right)]
        
        return dp(0, len_piles-1) > 0