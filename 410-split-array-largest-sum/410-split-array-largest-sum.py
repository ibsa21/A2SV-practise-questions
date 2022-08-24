class Solution:
    
    def findM(self, nums:List[int], candidate:int, m:int)->Tuple[int, int]:
        nums = nums + [float(inf)]
        curr_sum = 0
        for idx in range(len(nums)-1):
            curr_sum += nums[idx]
            if curr_sum + nums[idx + 1] > candidate:
                m-=1
                curr_sum = 0
        return m
    
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = low + (high - low)//2
            if self.findM(nums, mid, m)>=0:
                high = mid -1
            else:
                low = mid + 1
        return low
                
