class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """          
        
        candidates.sort()
        global_ans = []
        def backtrack(idx, curr_sum, local_ans, target):
            # print(curr_sum, target, idx)
            if  curr_sum > target: return
            if curr_sum == target:
                global_ans.append(local_ans[::])
                return

            for i in range(idx, len(candidates)):
                if i != idx and candidates[i] == candidates[i-1]: continue

                local_ans.append(candidates[i])
                backtrack(i+1,curr_sum+candidates[i], local_ans, target)
                local_ans.pop()

        backtrack(0, 0, [], target)
        return global_ans

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                