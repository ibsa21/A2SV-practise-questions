class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        #number of deletions
        number_of_deletion = 0
        for i in range(len(nums)-1):
            if (i-number_of_deletion) % 2 == 0 and nums[i]==nums[i + 1]:
                number_of_deletion += 1
        
        return number_of_deletion if (len(nums)-number_of_deletion) % 2 == 0 else number_of_deletion + 1