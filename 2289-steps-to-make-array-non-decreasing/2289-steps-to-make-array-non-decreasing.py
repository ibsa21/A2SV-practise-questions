class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        increasing_ms  = [(nums[0], 0)]             # type: List[Tuple[int, int]]
        global_steps_performed = 0

        for idx, num in enumerate(nums):
            if idx == 0: continue
            local_steps_performed  = 0

            while increasing_ms and increasing_ms[-1][0] <= num:
                local_steps_performed = max(local_steps_performed, increasing_ms.pop()[1])

            if increasing_ms: local_steps_performed += 1
            else:local_steps_performed = 0

            global_steps_performed = max(global_steps_performed, local_steps_performed)
            increasing_ms.append((num, local_steps_performed))
        return global_steps_performed
