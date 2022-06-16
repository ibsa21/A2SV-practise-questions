class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(l, r):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
    
        def dp():
            
            res = ''
            for i in range(len(s)):    
                odd = is_palindrome( i, i)
                even = is_palindrome(i, i + 1)

                res = max(res, odd, even, key = len)

            return res
        return dp()