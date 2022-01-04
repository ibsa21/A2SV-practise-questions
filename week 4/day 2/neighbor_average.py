import statistics
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        median = statistics.median(nums)
        length  = len(nums)
        odd = range(1, length, 2)
        even = range(0, length, 2)
        
        num = [0] * length
        j =0
        k = 0
        for i in range(length):
            if (nums[i] < median):
                print(odd[j], j)
                num[odd[j]] = nums[i]
                j += 1
            else:
                num[even[k]] = nums[i]
                k += 1
        nums = num
        return nums
        
