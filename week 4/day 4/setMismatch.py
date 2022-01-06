class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result=[]
        result=[x for x in range(1, len(nums)+1) if x not in nums]
        for key, values in Counter(nums).items():
            if values == 2:
                result.insert(0, key)
        return  result
