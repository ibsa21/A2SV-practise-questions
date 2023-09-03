class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        window_sum = 0
        left_pointer = 0
        output = float('inf')
        

        for right_pointer in range(len(nums)):
            window_sum += nums[right_pointer]

            while window_sum >= target:
                output = min(output, right_pointer-left_pointer+1)
                window_sum -= nums[left_pointer]
                left_pointer += 1


        return 0 if output == float('inf') else output