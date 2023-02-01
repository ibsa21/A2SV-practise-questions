class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)
        answer = max(scores)
        ages_scores = [(ages[i], scores[i]) for i in range(n)]
        ages_scores.sort()
        dp = []

        for i in range(n):
            dp.append(ages_scores[i][1])
            for j in range(i):
                if ages_scores[i][1] >= ages_scores[j][1]:
                    dp[i] = max(dp[i], dp[j]+ages_scores[i][1])
            answer = max(answer, dp[i])
        return answer
