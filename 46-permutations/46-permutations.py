from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(n,path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for i in nums:
                if i not in path:
                    # path += [i]
                    dfs(i,path+[i])
                    # path.pop()
        for i in nums:
            dfs(i,[i])
        return ans