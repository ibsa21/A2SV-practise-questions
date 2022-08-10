from bisect import bisect_left
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        ''' Approach: Dynamic Programming + Binary Search
            Time complexity: O(nlog(n))
            Space complexity: O(n)
        '''
        rides.sort()
        dp = [end-start+tip for start, end, tip in rides]
        startingPoint = [ride[0] for ride in rides]
        
        for i in range(len(rides)-2, -1, -1):
            idx = bisect_left(startingPoint, rides[i][1])
            maxValue = dp[idx] if idx < len(rides) else 0
            dp[i] = max(dp[i + 1], dp[i] + maxValue)
        return dp[0]