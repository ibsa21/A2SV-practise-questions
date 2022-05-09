class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [(int(x[:2])*60  + int(x[3:])) for x in timePoints]
        timePoints.sort()
        
        min_difference = 3600
        for i in range(len(timePoints)-1):
            min_difference = min(min_difference, timePoints[i+1]-timePoints[i])
        min_difference  = min(min_difference, abs(timePoints[len(timePoints)-1]-(1440 + timePoints[0])))
        return min_difference
            
            
        