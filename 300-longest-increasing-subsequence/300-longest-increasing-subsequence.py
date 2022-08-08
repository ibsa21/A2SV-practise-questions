class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        '''
            Very optimal solution: 
            Space complexity: O(max(longest_increasing))
            time complexity: O(nlogn)
            
        '''
        increasing_ds = []
        for idx, num in enumerate(nums):
            if not increasing_ds or num > increasing_ds[-1]:
                increasing_ds.append(num)
            else:
                idx_pos = bisect_left(increasing_ds, num)
                increasing_ds[idx_pos] = num
        return len(increasing_ds)
        '''
            Approach 1: True Dynamic programming
            Time complexity: O(n)
            Space complexity: O(n**2)
        '''
        dp = [1] * len(nums)
        for r_idx in range(len(nums)-2, -1, -1):
            local_max = dp[r_idx]
            for next_idx in range(r_idx + 1, len(nums)):
                if nums[next_idx] > nums[r_idx]:
                    local_max = max(local_max, dp[next_idx] + 1)
                dp[r_idx] = local_max
        
        return max(dp)
        '''
            Approach2: Depth first search + memoization/caching
            Space Complexity: O(n)
            Time complexity: O(n ** 2) -> Not sure
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