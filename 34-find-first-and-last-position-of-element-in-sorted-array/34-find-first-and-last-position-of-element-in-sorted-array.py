class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        
        def binary_search(left, right,):
            
            if left > right:
                return [-1, -1]
            
            mid = left + (right-left)//2
            if nums[mid]==target:
                start = mid
                end = mid
                while start > 0 and  nums[start-1]==target:
                    start -=1
                
                while end < len(nums)-1 and nums[end + 1]==target:
                    end  += 1
                    
                return [start, end]
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else:
                return binary_search(mid + 1, right)
            
        return binary_search(left, right)
        