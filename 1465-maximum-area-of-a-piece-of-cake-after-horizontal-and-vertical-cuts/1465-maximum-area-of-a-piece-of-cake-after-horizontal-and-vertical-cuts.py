class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        def get_max_diff(arr, h_w):
            max_column = max(0, arr[0])
            for idx, row in enumerate(arr):
                if idx != 0:
                    max_column = max(max_column, abs(row - arr[idx-1]))
            max_column = max(max_column, abs(h_w-arr[-1]))
            return max_column

        return (get_max_diff(horizontalCuts, h) * get_max_diff(verticalCuts, w)) % (pow(10, 9) + 7)