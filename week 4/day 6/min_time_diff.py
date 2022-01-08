class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [(int(x[:2])*60  + int(x[3:])) for x in timePoints]
        timePoints.sort()
        time_difference = []
        for i in range(len(timePoints)-1):
            time_difference.append(timePoints[i+1]-timePoints[i])
        time_difference.append(abs(timePoints[len(timePoints)-1]-(1440 + timePoints[0])))
        return min(time_difference)
            
            
        
