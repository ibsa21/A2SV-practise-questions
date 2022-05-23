class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def helper(a, char):
            for j in range(a, len(t)):
                if t[j] == char:
                    return j + 1
            return False
        a  = 0
        for i in range(len(s)):
            a = helper(a, s[i])
            if not a:return False
        return True
            