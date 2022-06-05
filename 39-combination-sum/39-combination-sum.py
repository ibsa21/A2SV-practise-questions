class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #time complexity O(2^target) and space complexity O(2^n)
        ans = []
        def backtrack(i, sumValue, comb):
            if i >= len(candidates) or sumValue > target:
                return 
            if sumValue == target:
                print(comb)
                ans.append(comb.copy())
                return

            comb.append(candidates[i])
            backtrack(i, sumValue + candidates[i], comb)
            comb.pop()
            backtrack(i + 1, sumValue, comb)
        backtrack(0, 0, [])
        return ans
                
            
            