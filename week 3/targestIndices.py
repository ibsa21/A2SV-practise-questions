class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices_list = []
        nums.sort()
        indices_list = [i for i, value in enumerate(nums) if value == target]
            
        return indices_list
        
