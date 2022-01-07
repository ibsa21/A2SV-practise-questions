class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = [ (dist[x]/speed[x]) for x in range(len(dist))]
        arrival_time.sort()
        
        t=0
        result = 0
        for time in arrival_time:
            if time <= t:
                break
            else:
                t += 1
                result +=1
        return result
