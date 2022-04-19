class Solution:
    def getDescentPeriods(self, nums: List[int]) -> int:
        
        result = 0
        count_smooth = 0
        i = 1
        total = 0
        while i < len(nums):
            count_smooth = 0
            is_looped = False
            while i < len(nums) and  nums[i - 1] - nums[i] == 1:
                i += 1
                count_smooth += 1
                is_looped = True
                total += 1
            
            if not is_looped:
                i += 1
            else:
                result += ((count_smooth + 2) * (count_smooth  + 1)) // 2
                total +=1
        return result + len(nums) - total