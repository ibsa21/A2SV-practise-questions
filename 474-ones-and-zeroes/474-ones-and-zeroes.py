class Solution:
    def count(self, S):
        zeros = 0
        ones = 0
        
        for s in S:
            if s == '1':
                ones += 1
            else:
                zeros += 1
        
        return zeros, ones
    
    def dp(self, strs, i, zeros, ones, dp):
        if i == len(strs):
            return 0
        
        if (i, zeros, ones) in dp:
            return dp[(i, zeros, ones)]
        
        count = self.count(strs[i])
        pick = -1
        if zeros - count[0] >= 0 and ones - count[1] >= 0:
            pick = 1 + self.dp(strs, i+1, zeros - count[0], ones - count[1], dp)
        
        dont = self.dp(strs, i+1, zeros, ones, dp)
        dp[(i, zeros, ones)] = max(pick, dont)
        return max(pick, dont)
            
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        return self.dp(strs, 0, m, n, dp)