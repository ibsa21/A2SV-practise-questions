class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        c = {i:() for i in range(len(strs))}
        for i in range(len(strs)):
            c[i] = (strs[i].count('0'), strs[i].count('1'))
            
        def dp(i, zeros, ones, memo):
            if i == len(strs):return 0
            if (i, zeros, ones) in memo:return memo[(i, zeros, ones)]

            count = c[i]
            pick = -1
            if zeros - count[0] >= 0 and ones - count[1] >= 0:
                pick = 1 + dp(i+1, zeros - count[0], ones - count[1], memo)

            dont = dp(i+1, zeros, ones, memo)
            memo[(i, zeros, ones)] = max(pick, dont)
            return max(pick, dont)

        return dp(0, m, n, {})