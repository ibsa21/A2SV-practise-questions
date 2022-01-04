import statistics
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        median = statistics.median(nums)
        odd = [x for x in range(1, len(nums), 2)]
        even = [x for x in range(0, len(nums), 2)]
        
        num = [0] * len(nums)
        j =0
        k = 0
        for i in range(len(nums)):
            if (nums[i] < median):
                print(odd[j], j)
                num[odd[j]] = nums[i]
                j += 1
            else:
                num[even[k]] = nums[i]
                k += 1
        nums = num
        return nums
        
