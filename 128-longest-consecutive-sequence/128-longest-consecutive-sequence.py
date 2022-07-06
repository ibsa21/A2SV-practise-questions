class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Time Complexity: O(n)
            Space Complexity: O(n)
        '''
        nums_set = set(nums)            # type; Set
        counted_nums = set()            # type: Set
        
        def count_less_num(num:int)->int:
            count = 1       # type: int
            while num -1 in nums_set and num -1 not in counted_nums:
                num -= 1
                counted_nums.add(num)
                count += 1
            return count
        
        def count_greater_num(num:int) -> int:
            count = 1       # type: int
            while num + 1 in nums_set and num + 1  not in counted_nums:
                num += 1
                counted_nums.add(num)
                count += 1
            return count
        
        longest_sequence = 0            # type: int
        for num in nums:
            if num not in counted_nums: 
                longest_sequence = max(longest_sequence, count_less_num(num) + count_greater_num(num)-1)
        return longest_sequence