from cmath import inf
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(set)
        visited = {}
        for source, target, time in times:
            adj_list[source].add((target, time))
            visited[source] = float(inf)
            visited[target] = float(inf)
        
        for key in adj_list:
            adj_list[key] = sorted(adj_list[key], key=lambda x: x[1])

        def dfs(source, curr_time):
            
            if curr_time < visited[source]:
                visited[source]  = curr_time
                for node, time in adj_list[source]:
                    dfs(node, curr_time + time)
        dfs(k, 0)

        result  = max(visited.values())
        return -1 if (result == float(inf) or len(visited.keys()) < n) else result
