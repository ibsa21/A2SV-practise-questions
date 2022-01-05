class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        listA = list(count.values())
        for i in range(1, len(set(nums))):
            index = 0
            for j in range(0, i):
                index += listA[j]
            nums[i], nums[index] = nums[index], nums[i]
            
        return len(set(nums))
