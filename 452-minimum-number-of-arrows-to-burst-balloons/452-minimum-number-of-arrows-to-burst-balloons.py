class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #your code if better
        #you could've optimized your solution
        
        if len(points) <2: return len(points)
        points.sort()  #O(nlogn)
        largeBallons = points[0][1]
        ans = 1
        
        for i in range(1, len(points)):   #O(N)
            if points[i][0]<=largeBallons:
                largeBallons = min(points[i][1],largeBallons)
                continue
                
            largeBallons=points[i][1]
            ans +=1 

        return ans