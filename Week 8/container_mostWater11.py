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
            
            
        """
          Algorithm: using two pointer approach
             step1: start left equal 0 and right equal length -1
             step2: iterate until left is equal to or greater than right
             step3: take  height of the area the as the minimum height of the two ends - because the water may overflow if we choose the largest one
             step4: width of area is equal to difference between two ends, Area = width * height
             step5: decide from where to change your window size - 
        """
