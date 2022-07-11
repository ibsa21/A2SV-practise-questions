class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        x = nums.index(max(nums))
        y = nums.index(min(nums))
        l = len(nums)
        
        #take minimum of 
            # removing number from left
            # removing number from right
            # removing number from both left and right
        return min(max(x+1,y+1), max(l-x,l-y), x+1+l-y, y+1+l-x)
        
        max_num_idx = nums.index(max(nums))
        min_num_idx = nums.index(min(nums))
        
        del_left = max_num_idx + 1
        del_right = len(nums)-min_num_idx
        
        minimum_operations = 0
        #removing from left, and right
        minimum_operations = del_left + del_right
        
        #removing from left onlyr
        minimum_operations = min(minimum_operations, max(max_num_idx + 1, min_num_idx + 1))
        
        #removing from right only
        minimum_operations = min(minimum_operations, max(len(nums)-min_num_idx, len(nums)-max_num_idx))
        
        return minimum_operations
        
        r
        print(del_left, del_right)
        
        deleted = sorted([max_num, min_num], key = lambda x: x[1])
        left, right = 0, len(nums)-1
        
        minimum_operation = 0
        for num, idx in deleted:
            if idx < left or idx > right: break
            if idx - left >= right - idx:
                minimum_operation += (right - idx + 1)
                right = idx-1
            else:
                minimum_operation += (idx - left + 1)
                left = idx + 1
        return minimum_operation