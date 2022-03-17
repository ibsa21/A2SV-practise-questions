class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        low = 1
        high  = sum(nums)
        min_divisor = high
        
        def divide_number(divisor):
            
            sum_result = 0
            
            for i in range(len(nums)):
                sum_result += math.ceil(nums[i]/divisor)
            
            
            if sum_result <= threshold:
                return True
            else:
                return False
        
        def binary_search(low, high):
            nonlocal min_divisor
            if low > high:
                return
            
            mid = low + (high-low)//2
            
            if divide_number(mid):
                min_divisor = min(min_divisor, mid)
                binary_search(low, mid-1)
            else:
                binary_search(mid + 1, high)
        binary_search(low, high)
        return min_divisor