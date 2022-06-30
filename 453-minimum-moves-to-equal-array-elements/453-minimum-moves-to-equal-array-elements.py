class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = 0                   # type: int
        min_num = 0                   # type: int
        number_moves = 0              # type: int
        
        nums.sort(reverse = True)
        for idx in range(len(nums)):
            increment_rate = (max_num - min_num)
            max_num = (nums[idx] + increment_rate)
            min_num = (nums[-1] + increment_rate)
            number_moves += increment_rate
        return number_moves
            
            