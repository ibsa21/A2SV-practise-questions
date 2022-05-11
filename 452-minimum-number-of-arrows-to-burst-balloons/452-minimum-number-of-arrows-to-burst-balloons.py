class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        for i in range(len(points)):
            points[i][0], points[i][1] = points[i][1], points[i][0]
        heapq.heapify(points)
        ans = 0
        while points:
            x_end, x_start = heapq.heappop(points)
            
            while points and points[0][1] <= x_end:
                heapq.heappop(points)
            ans +=1
        return ans