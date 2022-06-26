# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
            time complexity: O(logn)
            space complexity: O(1)
        """
        def binary_search():
            low, high, = 1, mountain_arr.length()-2
            while low <= high:
                mid:int  = low + (high - low)//2
                num_at_left:int = mountain_arr.get(mid-1)
                num_at_middle:int = mountain_arr.get(mid)
                num_at_right:int = mountain_arr.get(mid + 1)

                if num_at_left < num_at_middle < num_at_right: low = mid + 1
                elif num_at_left> num_at_middle > num_at_right: high = mid -1
                else:return mid  
        pivot_index  = binary_search()
        
        def binary_search_target(low:int, high:int, isleft:bool):
            while low <= high:
                mid:int = low + (high - low)//2
                num_at_middle = mountain_arr.get(mid)
                if num_at_middle == target: return mid
                elif num_at_middle > target: 
                    if not isleft:low = mid + 1
                    else:high = mid-1
                else: 
                    if isleft:low  = mid + 1
                    else:high = mid - 1
            return -1
        
        left_result:int = binary_search_target(0, pivot_index-1, True)
        if left_result != -1: return left_result
        return binary_search_target(pivot_index, mountain_arr.length()-1, False)