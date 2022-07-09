class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = [nums[0]]
        
        for idx, jump in enumerate(nums):
            local_max_reach = min(idx + jump, len(nums)-1)
            if idx != 0:
                max_reach.append(max(max_reach[idx-1], local_max_reach))
        
        current_reach = max_reach[0]
        step = 1 if len(nums) > 1 else 0
        while current_reach < len(nums)-1:
            current_reach = max_reach[current_reach]
            step += 1
        return step