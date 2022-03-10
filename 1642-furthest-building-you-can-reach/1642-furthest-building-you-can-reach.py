
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        height_heap = []
        used_bricks = 0
        
        for i in range(1, len(heights)):
            
            diff_value = heights[i]-heights[i-1]
            
            if diff_value > 0:
                heappush(height_heap, diff_value)
                
                ladders -= 1
                if ladders < 0:
                    used_bricks += heappop(height_heap)
                    
                if used_bricks > bricks:
                    return i - 1
                
        return len(heights)-1