class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        visited = [0] * len(nums)
        answer = []
        num = 0
        def backtrack(path):
            nonlocal num
            if len(path) == len(nums):
                answer.append(path.copy())
                return
            
            for index in range(len(nums)):
                
                if not num & (1 << index):
                    num = num | (1 << index)
                    backtrack(path+[nums[index]])
                    num = num & ~(1 << index)

        
        backtrack([])
        return answer