class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            Approach: Depth first search + memoization/caching
            Space Complexity: O(n)
            Time complexity: O()
        '''
        cache = {}                          # type: Dict[int, int]
        
        def dfs(idx:int, curr_count:int)->int:
            if idx in cache: return cache[idx] + curr_count
            
            curr_count += 1
            local_max = curr_count
            
            #iterate over possibilites of next index
            for next_idx in range(idx + 1, len(nums)):
                if nums[next_idx] > nums[idx]:
                    local_max = max(local_max, dfs(next_idx, curr_count))
            cache[idx] = local_max
            return cache[idx]
        
        global_max = 1
        for r_idx in range(len(nums)-1, -1, -1):
            global_max = max(global_max, dfs(r_idx, 0))
        return global_max