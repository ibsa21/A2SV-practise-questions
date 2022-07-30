class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        '''Optimal solution
           Time complexity: O(N)
           Space complexity: O(N)
        
        '''
        stack = []
        area_rectangle = 0
        for idx, height in enumerate(heights):
            left_idx = idx
            while stack and stack[-1][1] > height:
                left_idx, left_height  = stack.pop()
                area_rectangle = max(area_rectangle, (idx-left_idx) * left_height)
            stack.append((left_idx, height))
        
        for idx, height in stack:
            area_rectangle = max(area_rectangle, (len(heights)-idx) * height)
        return area_rectangle
                
        '''
            Bruteforce
            Time Complexity: O(n**2)
            Space Complexity: O(1)
        '''
        area_rectangle  = 0
        for n_cells in range(len(heights)):
            left_cell = 0
            for right_cell in range(len(heights)):
                if right_cell - left_cell + 1==n_cells + 1:
                    area_rectangle = max(area_rectangle, \
                                            min(heights[left_cell:right_cell + 1]) * (n_cells + 1))
                    left_cell += 1
        return area_rectangle
                