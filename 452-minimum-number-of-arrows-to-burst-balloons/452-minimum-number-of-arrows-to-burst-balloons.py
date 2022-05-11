class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #heap approach
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
    
        #sotring approach
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