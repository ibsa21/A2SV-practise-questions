class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        visited = [0] * len(nums)
        answer = []
        def backtrack(path):
            
            if len(path) == len(nums):
                answer.append(path.copy())
                return
            
            for index in range(len(nums)):
                if not visited[index]:
                    visited[index] = 1
                    backtrack(path+[nums[index]])
                    visited[index] = 0
        
        backtrack([])
        return answer