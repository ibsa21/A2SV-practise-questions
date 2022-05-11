class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        ans,i = 0,0
        while i < len(points):
            x_start, x_end = points[i]
            while i < len(points) and  points[i][0] <= x_end:
                i += 1
            ans += 1
        return ans