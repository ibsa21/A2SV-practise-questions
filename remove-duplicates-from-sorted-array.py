class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        leftPointer = 1

        for index in range(1, len(nums)):
            prev_left_value = nums[leftPointer-1]
            current_value = nums[index]

            if current_value != prev_left_value:
                nums[leftPointer] = current_value
                leftPointer += 1
        
        return leftPointer