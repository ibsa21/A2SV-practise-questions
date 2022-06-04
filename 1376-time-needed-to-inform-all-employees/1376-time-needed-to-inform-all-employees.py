class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        my_dict = defaultdict(list)
        
        for idx, chief in enumerate(manager):
            my_dict[chief].append(idx)
            
        def dfs(emp):
            time = informTime[emp]
            if not my_dict[emp]:return 0
            
            t = 0
            for sub in my_dict[emp]:
                t = max(t, dfs(sub))
            time += t
            return time
        
        return dfs(headID)    
