class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        nums.sort() 
        
        isposivite = lambda x, y: x>=0 and y >=0
        for i in range(1, len(nums)):
            if isposivite(nums[i], nums[i-1]) and nums[i] - nums[i-1] > 1:
                return nums[i-1] + 1
        
        return nums[-1] + 1
        
#         if max(nums) <= 0:return 1
        
#         pos_list = set()
#         min_posnumber = float(inf)
        
#         for num in nums:
#             if num > 0:pos_list.add(num)
        
#         for num in nums:
#             if num -1 > 0 and num-1 not in pos_list:
#                 min_posnumber = min(min_posnumber, num-1)
        
#         if min(pos_list) > 1: return 1
#         return min_posnumber if min_posnumber != float(inf) else max(pos_list) + 1
