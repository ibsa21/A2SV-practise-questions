import numpy as np
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[::]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.prefix_sum = np.array(nums)
        

    def update(self, index: int, val: int) -> None:
        change_value = val - self.nums[index]
        self.nums[index] = val
        self.prefix_sum[index:] += change_value

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right]- self.prefix_sum[left-1] if left > 0 else self.prefix_sum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)