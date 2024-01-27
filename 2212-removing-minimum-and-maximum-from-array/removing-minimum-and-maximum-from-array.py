class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        max_num = [-float('inf'), len(nums)]
        min_num = [float('inf'), len(nums)]

        for index, num in enumerate(nums):
            if num > max_num[0]:
                max_num = [num, index]
            if num < min_num[0]:
                min_num = [num, index]
        
        max_distance = max_num[1]+1
        if max_distance > len(nums) - max_num[1]:
            max_distance = - (len(nums) - max_num[1])

        min_distance = min_num[1]+1
        if min_distance > len(nums) - min_num[1]:
            min_distance = - (len(nums)-min_num[1])

        if min_distance * max_distance >= 0:
            return max(abs(max_distance), abs(min_distance))
        
        min_distance = abs(min_distance)
        max_distance = abs(max_distance)
        in_between_nums = len(nums) - min_distance - max_distance

        return min(min_distance + max_distance, min(min_distance, max_distance) + in_between_nums + 1)