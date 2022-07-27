class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        
        while left < right:
            width = right - left
            
            height_t = height[left] if height[left] < height[right] else height[right]
            max_area = max(max_area, height_t * width)
            #print(width, height_t, max_area)
            #print(left, right, max_area)
            
            if (height[left] > height[right]):
                right -= 1
            else:
                left += 1
        
        return max_area
            
            
        