from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
            Approach: Dynamic Programming (Bottom Up) + Binary Search
            Time complexity: O(nlog(n))
            Space complexity: O(n)
        '''
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort()
        
        startTime, dp = [], []
        for start, end, profit in jobs:
            startTime.append(start)
            dp.append(profit)
            
        for i in range(len(jobs)-2, -1 , -1):
            idx = bisect_left(startTime, jobs[i][1])
            prev_value = dp[idx] if idx < len(jobs) else 0
            dp[i] = max(dp[i + 1], prev_value + dp[i])
        return dp[0]