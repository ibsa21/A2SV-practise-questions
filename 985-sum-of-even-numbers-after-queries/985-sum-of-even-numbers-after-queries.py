class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even:int = sum(num for num in nums if num %2==0)
        result_array = []                   # type: List
        
        for num, idx in queries:
            before_change = nums[idx]
            nums[idx]  = before_change + num
            if (before_change + num) %2==0:
                if before_change %2==0:sum_even += num
                else:sum_even += (before_change + num)
            elif before_change %2==0:
                sum_even -= before_change
            result_array.append(sum_even)
        return result_array