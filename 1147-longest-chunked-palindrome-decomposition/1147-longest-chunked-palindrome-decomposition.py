class Solution:
    def longestDecomposition(self, s: str) -> int:
        s = list(s)
        l, r, ans = 0, len(s)-1, 0
        
        while l <= r:
            x, y = r, l
            while ''.join(s[y:l + 1]) != ''.join(s[r:x + 1]):
                r -= 1
                l += 1
            ans += 2
            if l >= r and  ''.join(s[y:l + 1])== ''.join(s[r:x + 1]) and  (x,r)== (l, y): ans -=1
            l += 1
            r -= 1
        return ans