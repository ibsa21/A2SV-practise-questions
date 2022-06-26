class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def binary_search():
            low, high, = 1, len(arr)-2
            while low <= high:
                mid:int  = low + (high - low)//2
                if arr[mid-1] < arr[mid] < arr[mid + 1]: 
                    low = mid + 1
                elif arr[mid-1]> arr[mid] > arr[mid + 1]: high = mid -1
                else:
                    return mid      
        return binary_search()
        
                    
        for idx in range(1, len(arr)-1):
            if arr[idx-1] < arr[idx] > arr[idx + 1]: return idx