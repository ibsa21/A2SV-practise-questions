class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        index_distance = []
        
        def ecludian_distance(x, y):
            return (x**2 + y**2)**0.5
        
        for i, xy in enumerate(points):
            heapq.heappush(index_distance, (ecludian_distance(xy[0], xy[1]), i))
        
        return [points[i] for x, i in heapq.nsmallest(k, index_distance)]