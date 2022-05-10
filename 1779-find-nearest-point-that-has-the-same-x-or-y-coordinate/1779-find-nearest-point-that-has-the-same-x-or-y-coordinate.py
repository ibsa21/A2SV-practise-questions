class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        def distance(xi, yi):
            return abs(x - xi) + abs(y - yi)
        
        result = (None, -1)
        for i, cord in enumerate(points):
            xi, yi = cord
            if xi==x or yi==y:
                dist = distance(xi, yi)
                if result[0]==None or dist < result[0]:
                    result = (dist, i)
                    
        return result[1]
                