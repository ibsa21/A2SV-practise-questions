class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        for idx, points in enumerate(cardPoints):
            if idx !=0:
                cardPoints[idx] +=(cardPoints[idx-1])
                
        total_sum = cardPoints[-1]
        max_difference:int = -float(inf)
        len_removed = len(cardPoints)-k
        
        for idx in range(len_removed-1, len(cardPoints)):
            left = cardPoints[idx-len_removed] if idx-len_removed > -1 else 0
            right = cardPoints[idx]
            max_difference  = max(max_difference, total_sum - (right - left))
        return max_difference
            