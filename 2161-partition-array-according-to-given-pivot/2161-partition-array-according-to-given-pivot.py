#first approach
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        result = [None] * len(nums)
        
        left_count = 0
        right_count = 0
        
        for num in nums:
            if num < pivot:
                left_count += 1
            elif num > pivot:
                right_count += 1
                
        left = 0
        right = len(nums) - right_count
        
        p_index = left_count
        for num in nums:
            
            if num < pivot:
                result[left]  = num
                left += 1
            elif num > pivot:
                result[right] = num
                right += 1
            else:
                result[p_index] = num 
                p_index += 1
        return result

    #second approach
    class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        lessthan = []
        greaterthan  = []
        equal_pivot = []
        
        for num in nums:
            if num < pivot:
                lessthan.append(num)
                
            elif num > pivot:
                greaterthan.append(num)
            else:
                
                equal_pivot.append(num)
        
        lessthan.extend(equal_pivot)
        lessthan.extend(greaterthan)
        
        return lessthan
