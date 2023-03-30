class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        visited = set()
        answer = []
        def backtrack(path):
            
            if len(path) == len(nums):
                answer.append(path.copy())
                return
            
            for index in range(len(nums)):
                if index not in visited:
                    visited.add(index)
                    backtrack(path+[nums[index]])
                    visited.remove(index)
        
        backtrack([])
        return answer