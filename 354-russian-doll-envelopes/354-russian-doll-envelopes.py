class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        def find_range(arr, width_target):
            
            def binary_search(low, high):
                if low > high:return low
                
                mid = low + (high-low)//2
                
                if arr[mid]== width_target:
                    return mid
                elif arr[mid] < width_target:
                    return binary_search(mid + 1, high)
                else:
                    return binary_search(low, mid-1)
            return binary_search(0, len(arr)-1)
            
        envelopes.sort(key= lambda x: (x[0], -x[1]))
        res_list = []
        
        for height, width in envelopes:
            left = find_range(res_list, width)
            if left == len(res_list):
                res_list.append(width)
            else:
                res_list[left] = width
        return len(res_list)